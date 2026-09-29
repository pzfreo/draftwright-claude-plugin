# Draftwright for Claude

Draftwright turns a STEP model into a technical drawing that you can inspect with Claude, revise, and download as a PDF. This plugin combines a small drawing workflow skill with Draftwright's authenticated remote MCP connector. It works in Claude chat and other Claude surfaces that support remote connectors. The interactive MCP App shows upload, drawing preview, findings, and PDF actions inside the conversation where supported.

Connect your Draftwright account through OAuth. When you upload a STEP file, the file goes from your device to Draftwright. The connector sends drawing jobs and results to your Draftwright account; Claude receives the drawing image and review findings when it calls the review tool. The plugin contains no local executable or credentials. If the in-chat card is unavailable, the connector provides private, expiring browser links for upload and PDF download.

## Install and use

For Claude chat, the tested connection path is **Customize → Connectors → Add custom connector**. Enter `https://mcp.draftwright.io/mcp-stateless`, then sign in to your Draftwright account. You can use the in-chat upload and drawing viewer without installing a plugin.

To add the drawing skill as a plugin, open **Customize → Plugins → Add marketplace**, enter `https://github.com/pzfreo/draftwright-claude-plugin`, and add **Draftwright**. The plugin declares the same remote MCP endpoint. Check its connector status and complete OAuth if Claude asks you to connect it. If you already connected Draftwright directly, keep using that working connection.

In Claude Code, the equivalent commands are:

```text
claude plugin marketplace add pzfreo/draftwright-claude-plugin
claude plugin install draftwright@draftwright-marketplace
```

The GitHub-generated source ZIP is a repository snapshot, not a tested plugin upload package; use the marketplace route above. The plugin manifest and local marketplace installation have been validated with Claude Code 2.1.284. Claude chat marketplace activation still needs an end-to-end test.

Ask Claude to “make a technical drawing from my STEP file” to start. The drawing still needs your review for manufacturing intent, such as material, tolerances, and finish.

Source: [Draftwright](https://draftwright.io). Licensed under MIT.
