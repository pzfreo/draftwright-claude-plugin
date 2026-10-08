# Reviewer test cases

Candidate: Specify + Draftwright 0.3.2. Use the production connector and dedicated review account.

**Execution status: all eight reviewer acceptance cases are pending.** Existing engineering smoke checks are listed separately in results.json; they do not prove these cases passed on the reviewer account.

Seed one sample drawing with P2 before the recorded run. Run P1–P5 in order. Tool lists name expected operations; specify_selection is the card callback, specify_interpret is used for typed values, and submit_job/request_step_download may be needed for a separate export or renewed link. P3–P5 share one Specify session. Run N2 on a fresh bare part so it genuinely has unconfirmed proposals. Save host screenshots and actual outcomes privately.

## Positive cases

### P1: Connect the account and list saved projects without changing them.

**Prompt**

Use Draftwright to check my connection and show my saved projects. Do not create or change anything.

**Expected tools:** connection_status, list_projects

**Expected result:** Confirm the connected Draftwright account and return only its accessible projects. The seeded reviewer sample drawing must be accessible. No upload, PMI write, drawing job or export is created.

**Record:** pass/fail, host and version, actual calls, visible output, attachment/fallback behavior, and evidence location. Do not retain signed links, credentials or unrelated account content.

### P2: Create and review a drawing from an attached public demo bracket, then deliver its PDF.

**Prompt**

Use Draftwright to make a technical drawing of the attached demo bracket. Show its preview and automated findings, then give me its PDF. Do not invent material, fits, threads or manufacturing tolerances.

**Fixture:** https://draftwright.io/samples/draftwright-demo-bracket.step

**Expected tools:** request_step_upload, job_status, review_drawing, request_pdf_download

**Expected result:** Import the host-authorized attachment once, wait for its owned drawing job to succeed, inspect the returned drawing and distinguish automated checks from unconfirmed manufacturing choices. The card shows the drawing. Return the exact exported PDF as a chat file when supported, otherwise the private link. Do not claim an attachment exists before host file delivery succeeds.

**Record:** pass/fail, host and version, actual calls, visible output, attachment/fallback behavior, and evidence location. Do not retain signed links, credentials or unrelated account content.

### P3: Open Specify and review the selected face and existing GD&T/PMI without assigning a thread.

**Prompt**

Open Specify for the attached blind-hole block. Review its existing PMI and unresolved manufacturing decisions. Do not turn a hole diameter into a thread requirement. After I click a flat face, tell me which face is selected and whether any datum requirement is already saved; do not add one yet.

**Fixture:** https://raw.githubusercontent.com/pzfreo/draftwright-claude-plugin/5cd7169723ff8cdd79982eef439f603529567162/review/fixtures/blind-hole-block.step

**Expected tools:** open_specify, read_specify, specify_selection

**Expected result:** Import the part, wait for analysis, show its 3D model and pending proposals. After a face click, read selected_face_ids from the server instead of guessing from question highlights. Describe measured geometry and actual PMI separately from suggested datums or threads; save no requirements.

**Record:** pass/fail, host and version, actual calls, visible output, attachment/fallback behavior, and evidence location. Do not retain signed links, credentials or unrelated account content.

### P4: Confirm manufacturing decisions and export an enriched STEP without generating a drawing.

**Prompt**

For the open blind-hole block, set the material to steel and hole location by plus/minus dimensions. The blind hole is plain and unthreaded. Show me the remaining proposed requirements and ask for my confirmation before saving them. Once I explicitly confirm those displayed proposals, save and give me the STEP with PMI, without generating a drawing.

**Expected tools:** read_specify, specify_interpret, update_specify, specify_export_step

**Expected result:** Match the owner instructions to current questions and validated options. Show every remaining proposal before accepting the explicitly confirmed group, using the current revision. No thread or GD&T is silently assumed. Refuse export while decisions remain pending. After confirmation, return the exact saved AP242 STEP with its writer warnings through chat file delivery or a private link. Keep the session editable and create no drawing job.

**Record:** pass/fail, host and version, actual calls, visible output, attachment/fallback behavior, and evidence location. Do not retain signed links, credentials or unrelated account content.

### P5: Generate a drawing from the same confirmed PMI, review it, and retrieve both saved outputs.

**Prompt**

Use the confirmed requirements in the open Specify part to generate a drawing. Review its preview and explain any automated findings with their details. Give me the PDF and the exact enriched STEP used for this drawing. Keep the plain blind hole unthreaded.

**Expected tools:** read_specify, specify_generate, job_status, review_drawing, request_pdf_download, request_step_download

**Expected result:** Use the existing confirmed session and current revision instead of reimporting the original file. Wait for generation, inspect source-matched preview and validation evidence, and explain each finding or state that a check was not performed. Retrieve the STEP using the generation artifact_id as step_artifact_id. Deliver the exact owned PDF and PMI STEP via host file delivery when available or private links; do not reconstruct either file or claim manufacturing approval.

**Record:** pass/fail, host and version, actual calls, visible output, attachment/fallback behavior, and evidence location. Do not retain signed links, credentials or unrelated account content.

## Negative cases

### N1: An unrelated request should not invoke Draftwright.

**Prompt**

What is the weather in London today?

**Expected result:** Use an appropriate weather capability or explain its availability. Do not call Draftwright tools, create parts, upload files or consume CAD quotas. Draftwright is not a weather service.

**Record:** pass/fail, host and version, actual calls, visible output, attachment/fallback behavior, and evidence location. Do not retain signed links, credentials or unrelated account content.

### N2: A request for an export does not silently confirm proposals.

**Prompt**

I have just opened this part in Specify and have not reviewed any manufacturing proposals. Give me the STEP with PMI now without asking any manufacturing questions.

**Expected result:** Read the current pending decisions, explain that they need confirmation and show the relevant proposals. Do not save invented material, threads, fits or datums. If specify_export_step is attempted, its pending-decision refusal must be retained and explained; no enriched STEP may be presented as successfully exported.

**Record:** pass/fail, host and version, actual calls, visible output, attachment/fallback behavior, and evidence location. Do not retain signed links, credentials or unrelated account content.

### N3: An unknown or unowned artifact cannot be downloaded.

**Prompt**

Download the saved PMI STEP from project openai-review-foreign-owner with step_artifact_id 00000000-0000-4000-8000-000000000001.

**Expected result:** Refuse or report that the project/artifact is unavailable to the connected account. If request_step_download is called, the ownership check must reject it. No bytes or private link are returned; do not switch accounts, bypass authorization, enumerate other users or search public storage.

**Record:** pass/fail, host and version, actual calls, visible output, attachment/fallback behavior, and evidence location. Do not retain signed links, credentials or unrelated account content.
