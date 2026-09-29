# Draftwright for Claude

Draftwright turns a STEP model into a technical drawing that you can inspect with Claude, revise, and download as a PDF. This plugin combines a small drawing workflow skill with Draftwright's authenticated remote MCP connector. It works in Claude chat and other Claude surfaces that support remote connectors. The interactive MCP App shows upload, drawing preview, findings, and PDF actions inside the conversation where supported.

Connect your Draftwright account from the plugin's Connectors tab. When you upload a STEP file, the file goes from your device to Draftwright. The connector sends drawing jobs and results to your Draftwright account; Claude receives the drawing image and review findings when it calls the review tool. The plugin contains no local executable or credentials. If the in-chat card is unavailable, the connector provides private, expiring browser links for upload and PDF download.

## Install and use

Until the plugin is listed in Claude's directory, download this repository as a ZIP. In Claude, open **Customize → Plugins → Add → Upload plugin** and select the ZIP. Then connect Draftwright from the plugin's **Connectors** tab. You will sign in to your own Draftwright account through OAuth. The plugin skill and connector can then be used in chat; the MCP App card appears when the client supports it.

Ask Claude to “make a technical drawing from my STEP file” to start. The drawing still needs your review for manufacturing intent, such as material, tolerances, and finish.

Source: [Draftwright](https://draftwright.io). Licensed under MIT.
