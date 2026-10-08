#!/usr/bin/env python3
"""Build the public plugin ZIP and separate reviewer test pack from this checkout."""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path
from urllib.parse import urlsplit
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_FILES = (
    'plugin.json', 'mcp.json', 'README.md', 'LICENSE',
    'skills/create-technical-drawing/SKILL.md', 'skills/specify-part/SKILL.md',
    'assets/logo.png', 'assets/icon.png',
)
REVIEW_FILES = (
    'README.md', 'cases.md', 'reviewer-access.md', 'demo-walkthrough.md',
    'results.json', 'fixtures/README.md', 'fixtures/demo-bracket.step',
    'fixtures/blind-hole-block.step',
)


def https_url(value: str) -> None:
    url = urlsplit(value)
    if url.scheme != 'https' or not url.hostname or url.username or url.password:
        raise ValueError(f'Expected a public HTTPS URL: {value}')


def validate() -> dict:
    manifest = json.loads((ROOT / 'plugin.json').read_text())
    ext = manifest['extensions']['com.openai']
    interface = ext['interface']
    limits = {'displayName': 30, 'shortDescription': 30, 'longDescription': 4000,
              'developerName': 80}
    for name, limit in limits.items():
        if not isinstance(interface[name], str) or not 0 < len(interface[name]) <= limit:
            raise ValueError(f'{name} must have 1–{limit} characters')
    if not interface['category']:
        raise ValueError('Category is required')
    for name in ('websiteURL', 'supportURL', 'privacyPolicyURL', 'termsOfServiceURL'):
        https_url(interface[name])
    for name in ('logo', 'composerIcon'):
        relative = interface[name]
        if not relative.startswith('./') or relative[2:] not in PLUGIN_FILES:
            raise ValueError(f'{name} must reference an included asset')
        data = (ROOT / relative).read_bytes()
        if data[:8] != b'\x89PNG\r\n\x1a\n' or len(data) > 5 * 1024 * 1024:
            raise ValueError(f'Invalid PNG asset: {name}')
        width, height = struct.unpack('>II', data[16:24])
        if width != height or not 48 <= width <= 4096:
            raise ValueError(f'{name} must be a square 48–4096px PNG')
    prompts = interface.get('defaultPrompt', [])
    if len(prompts) > 3 or len(set(prompts)) != len(prompts) or any(len(x) > 128 for x in prompts):
        raise ValueError('Invalid starter prompts')
    servers = json.loads((ROOT / 'mcp.json').read_text())['mcpServers']
    if len(servers) != 1 or servers['draftwright']['url'] != 'https://mcp.draftwright.io/mcp-stateless':
        raise ValueError('Review cases require the single production MCP server')
    cases = ext['review']['test_cases']
    if len(cases['positive']) != 5 or len(cases['negative']) != 3:
        raise ValueError('Initial MCP review requires five positive and three negative cases')
    for kind in ('positive', 'negative'):
        for case in cases[kind]:
            for name in ('description', 'prompt', 'expected_behavior'):
                if not case.get(name):
                    raise ValueError(f'Missing {name} in {kind} case')
            if kind == 'positive' and not case.get('tools_triggered'):
                raise ValueError('Positive cases require expected tools')
            for url in case.get('file_attachment_urls', []):
                https_url(url)
    if any(name in ext['review'] for name in ('test_credentials', 'reviewer_instructions')):
        raise ValueError('Reviewer access belongs in the secure dashboard, outside the plugin ZIP')
    if 'apps' in ext or 'hooks' in ext:
        raise ValueError('Public submissions must use MCP URLs, not app mappings or lifecycle hooks')
    if not ext['publication']['release_notes']:
        raise ValueError('Release notes are required')
    for name in PLUGIN_FILES:
        if not (ROOT / name).is_file():
            raise ValueError(f'Missing package file: {name}')
    return manifest


def archive(path: Path, files: dict[str, bytes]) -> None:
    with ZipFile(path, 'w', ZIP_DEFLATED) as bundle:
        for name, data in sorted(files.items()):
            entry = ZipInfo(name, (2026, 10, 8, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            bundle.writestr(entry, data)
    with ZipFile(path) as bundle:
        if bundle.testzip() is not None or set(bundle.namelist()) != set(files):
            raise ValueError(f'Archive integrity failed: {path}')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    manifest = validate()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    version = manifest['version']
    plugin = args.output_dir / f'draftwright-plugin-{version}-submission.zip'
    test_pack = args.output_dir / f'draftwright-review-test-pack-{version}.zip'
    archive(plugin, {name: (ROOT / name).read_bytes() for name in PLUGIN_FILES})
    archive(test_pack, {name: (ROOT / 'review' / name).read_bytes() for name in REVIEW_FILES}
            | {'test-cases.json': json.dumps(manifest['extensions']['com.openai']['review']['test_cases'], indent=2).encode()})
    checksums = args.output_dir / 'SHA256SUMS'
    checksums.write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in (plugin, test_pack)))
    print(f'Package checks passed: {plugin}')
    print(f'Reviewer test pack: {test_pack}')
    print('Submission still requires publisher/domain verification, a dedicated reviewer login,')
    print('all eight acceptance cases on that account, an accessible demo recording, and portal scans.')


if __name__ == '__main__':
    main()
