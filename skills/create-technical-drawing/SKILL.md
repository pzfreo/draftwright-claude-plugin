---
name: create-technical-drawing
description: Create, inspect, revise, or download a Draftwright technical drawing from a STEP model. Use when the user asks for a manufacturing drawing, drawing review, or PDF of a STEP part.
---

# Create a technical drawing with Draftwright

Use the Draftwright connector. Each user connects their own Draftwright account through OAuth.

1. For a STEP already attached to chat, call `request_step_upload(file=...)` with its host-authorized file reference. It imports the file and returns `project_id` and `inspection_job_id`; the card follows that job automatically. Do not ask for another upload or paste file bytes into tool arguments. For a STEP file on the user's device, call `request_step_upload`. Use the returned in-chat card for upload. If the card is unavailable, give the private browser upload link. Do not ask the user to paste STEP data into the chat. If the user named an existing project, pass its `project_id`; otherwise start a new project.
2. The card uploads the file, follows the drawing job, and displays the sheet when ready. For a browser-link upload, check `step_upload_status` using its `upload_id`, then `job_status` using the returned project and job IDs. Wait for success before reviewing or exporting.
3. When you need to discuss the actual drawing, call `review_drawing` with the completed `job_id` and `project_id`. Inspect the returned image and findings. Distinguish geometry observed in the STEP file from manufacturing choices the owner has not supplied. Never invent material, tolerance, fit, thread, finish, or process requirements.
4. Describe concrete drawing issues and ask only questions that affect the drawing or quotation. Read the returned `validation` evidence: syntax, rendering, source consistency, reported coverage, layout and manufacturing decisions are separate checks. Unknown or unchecked results remain unknown; clean lint does not establish manufacturing approval. Before editing source, call `drawing_api_reference` for the installed DSL and its relevant examples. Read the full `drawing_source`, make the smallest justified edit, and save it with `persist_script` using the current script version as its parent. Its `valid` flag checks declarative syntax and allowed operations. Render that new version with `submit_job`, wait for `job_status`, and inspect it with `review_drawing`. On failure, use the returned bounded diagnostics and reference to correct the named declaration; never present an earlier PDF as the failed revision's output.
5. The card offers PDF download for a completed drawing. For clients without the card, submit an `export_drawing` job if needed, wait for success, then use `request_pdf_download` for that export job and give the returned private link. Do not paste PDF bytes or private link tokens into a public document.

Keep the reply short: what the drawing shows, any specific issue or owner decision, and where to view or download it. If an action is still running, say so instead of claiming the drawing is ready.

For quotation caveats, use the reference's ordinary authored NOTES recipe. Keep imported document statements, manufacturing requirements and their source identities intact. A new prose note has no CAD/PMI provenance or measurement-coverage claim. Change manufacturing requirements through Specify with the owner's confirmed intent.

For requests to check or change GD&T/PMI, use Specify to review existing requirements, confirm intended changes, and write them back into STEP. Use `specify_export_step` for a downloadable enriched STEP without creating a drawing. If generation already returned its enriched STEP artifact, use `request_step_download(step_artifact_id, project_id)` for that exact file. Keep the distinction between a drawing-source revision and a change to the model’s PMI explicit.
