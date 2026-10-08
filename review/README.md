# Specify + Draftwright review pack

Candidate version: 0.3.2. Production MCP: https://mcp.draftwright.io/mcp-stateless

Use this archive as the reviewer/operator test pack. Upload the separate plugin
submission ZIP to OpenAI. The plugin ZIP contains metadata, two skills, MCP
configuration and icons. This test pack contains access instructions, fixture
models, five positive and three negative cases, a recording plan and execution
status. No credentials are included in either archive.

## Preparation

1. Verify the publisher identity and choose the owning OpenAI organization/project.
2. Provision a dedicated production email/password reviewer account with a confirmed
   email, no MFA/code/magic-link dependency, and sufficient normal beta quota. Keep
   its credentials in an approved secret store and enter them only in the secure
   portal Review details form. No dedicated reviewer account is verified yet.
3. Upload the submission ZIP, then connect its MCP server and satisfy the exact
   domain challenge provided by the portal. Do not reuse an unrelated token.
4. Complete automated package, skill and tool scans, and correct findings.
5. Run every case using that dedicated account in the supported ChatGPT and Codex
   surfaces. Record actual outcomes in results.json; do not mark a skipped case
   passed. Host-specific visual cards/file attachments must be checked separately
   from server binary delivery.
6. Record the walkthrough and enter its accessible URL in Review details, or add
   review.demo_recording_url to the manifest and rebuild the ZIP. No recording URL
   is currently supplied; no placeholder URL is included in the manifest.
7. Review country availability and the proposed Productivity category in the portal.
   The package does not silently restrict countries or declare a verified publisher.
8. Submit for review only after the account, cases, recording, required scans and
   policy attestations are complete. Publish only after approval.

## Files

- cases.md / test-cases.json: the same five positive and three negative cases
  imported by the plugin manifest.
- reviewer-access.md: exact OAuth login flow and dedicated-account setup fields.
- demo-walkthrough.md: recording sequence and observable checks.
- results.json: honest execution status and existing engineering evidence.
- fixtures/: synthetic/public sample STEP models and SHA-256 values.

Working-session limits: three open Specify parts per account, 20 distinct PMI
writes per rolling day, seven-day working sessions, 25 MB raw STEP input. Run
P3–P5 on one part and close only test-owned parts when finished. Never loosen
production quotas, enumerate users, or use customer CAD data for review.

If an export fails, retain its actionable error and saved decisions. Do not draw
the original part as if it contained those decisions, reconstruct a PDF/STEP, or
remove requirements to force a successful export. Writer warnings and drawing
checks are evidence to discuss, not manufacturing approval.

## Official references

- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/plugin-guidelines
- https://developers.openai.com/plugins/build/plugins

Field requirements checked against official documentation on 2026-10-08.
