---
name: create-technical-drawing
description: Create, inspect, revise, or download a Draftwright technical drawing from a STEP model. Use when the user asks for a manufacturing drawing, drawing review, or PDF of a STEP part.
---

# Create a technical drawing with Draftwright

Use the Draftwright connector. Each user connects their own Draftwright account through OAuth.

1. For a STEP file on the user's device, call `request_step_upload`. Use the returned in-chat card for upload. If the card is unavailable, give the private browser upload link. Do not ask the user to paste STEP data into the chat. If the user named an existing project, pass its `project_id`; otherwise start a new project.
2. The card uploads the file, follows the drawing job, and displays the sheet when ready. For a browser-link upload, check `step_upload_status` using its `upload_id`, then `job_status` using the returned project and job IDs. Wait for success before reviewing or exporting.
3. When you need to discuss the actual drawing, call `review_drawing` with the completed `job_id` and `project_id`. Inspect the returned image and findings. Distinguish geometry observed in the STEP file from manufacturing choices the owner has not supplied. Never invent material, tolerance, fit, thread, finish, or process requirements.
4. Describe concrete drawing issues and ask only questions that affect the drawing or quotation. Do not describe the sheet as correct solely because automated lint passed. If the user requests a change, read the full `drawing_source`, make the smallest justified edit, and save it with `persist_script` using the current script version as its parent. Render that new version with `submit_job`, wait for `job_status`, and inspect it with `review_drawing`. Re-rendering the old script does not change the drawing.
5. The card offers PDF download for a completed drawing. For clients without the card, submit an `export_drawing` job if needed, wait for success, then use `request_pdf_download` for that export job and give the returned private link. Do not paste PDF bytes or private link tokens into a public document.

Keep the reply short: what the drawing shows, any specific issue or owner decision, and where to view or download it. If an action is still running, say so instead of claiming the drawing is ready.
