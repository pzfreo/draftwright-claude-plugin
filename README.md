# Specify + Draftwright

This plugin combines Specify's manufacturing requirements workflow with
Draftwright's technical drawing workflow through an authenticated remote MCP
server. Chat handles questions and decisions. The visual card shows the part,
explicit face selections and the resulting drawing where the host supports MCP
Apps. Ask in chat for the PDF or STEP with confirmed PMI. The assistant delivers
the exact exported file as a chat download when the host supports file delivery,
with a private download link as fallback.

## Beta release

Version 0.3.1 updates both skills to deliver exported PDFs and PMI STEP files
through chat. Version 0.3.0 added Specify guidance, host-authorized chat
attachments, GD&T review and durable sessions. The compact card without download
buttons is being tested on preview; production cards may still show the buttons.

Connect your Draftwright account through OAuth. Attach a STEP file in a host that
supports authorized file references, or use the card's upload action. The plugin
contains no executable or credentials. The server limits raw STEP inputs to 25 MB.
Browser handoff links remain available when a host cannot display the card.

Ask:

- “Specify the manufacturing requirements for this part.”
- “Review the GD&T and save a STEP with confirmed PMI.”
- “Make a technical drawing from this STEP file.”

Specify proposes manufacturing choices; the assistant must obtain acceptance
before saving them. A clean automated drawing check is not manufacturing approval.
Review dimensions, tolerances and requirements before sharing a drawing.

The beta allows three open Specify parts per account and 20 distinct PMI writes
per rolling day. Working sessions last seven days and recover after server
restarts. Retrying an interrupted write uses its saved operation. Ask to close a
working part when you no longer need it; saved drawing and STEP artifacts remain
available through their project/artifact IDs.

### Known beta limitation

Specify can inspect closed internal cavities represented as `BREP_WITH_VOIDS`,
but the current PMI writer cannot export them. This is tracked in
[Specify issue #12](https://github.com/pzfreo/specify-core/issues/12). If export
fails, keep the original part and saved requirements; do not remove requirements
just to get a file out.

## Claude

The tested connector route is **Customize → Connectors → Add custom connector**.
Enter `https://mcp.draftwright.io/mcp-stateless` and complete Draftwright OAuth.
Refresh the connection after a server update to load its latest tool definitions.

To add the skills, use this repository as a Claude plugin marketplace. Claude Code:

```text
claude plugin marketplace add pzfreo/draftwright-claude-plugin
claude plugin install draftwright@draftwright-marketplace
```

Complete OAuth for the plugin's connector. If a direct connector already works,
keep that connection and avoid duplicate Draftwright connectors.

## Portable package

`plugin.json`, `mcp.json` and the `skills/` folder supply the portable plugin
manifest and two workflows. A release ZIP should include those files with this
README and LICENSE at its root. Claude's `.claude-plugin` and `.mcp.json` remain
for its marketplace installation.

The portable package supports hosts implementing this plugin format and remote
MCP OAuth. Visual card and chat attachment capabilities depend on the host.
Installing a new ZIP updates packaged skills; refreshing an MCP connection updates
server tools.

For Codex's remote MCP connection:

```sh
codex mcp add draftwright --url https://mcp.draftwright.io/mcp-stateless/
codex mcp login draftwright
```

Source: [Draftwright](https://draftwright.io). Licensed under MIT.
