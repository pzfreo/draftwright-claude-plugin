# Reviewer access instructions

Supply these instructions and the dedicated account credentials in the secure
OpenAI Review details form. This document is outside the public plugin ZIP and
contains no actual credentials.

## Login flow

1. Install/connect Specify + Draftwright in the supported host, or choose Connect
   for the declared server in the OpenAI Plugins dashboard.
2. Use the production server URL https://mcp.draftwright.io/mcp-stateless.
3. OAuth opens a generated https://draftwright.io/oauth/consent request. Start this
   from the host; visiting the consent URL directly has no authorization request.
4. If an existing personal browser session is present, use an isolated browser
   profile or sign out before testing. Ensure the dedicated reviewer identity is
   used rather than a developer/customer account.
5. Enter the supplied existing-account Email and Password and choose Sign in with
   email. Google sign-in is optional and is not required for this review path.
6. Choose Allow connection. Wait for the redirect back to the initiating host.
7. Run P1. An empty saved-project list on a new account is valid; P2 creates the
   first owned sample drawing and P3 creates the Specify working part.

## Secure fields to complete

- Reviewer account email: supply privately in portal.
- Reviewer account password: supply privately in portal.
- Login URL: OAuth-generated https://draftwright.io/oauth/consent.
- Workspace/tenant: individual Draftwright account; use only its owned projects.
- Data: attach the included synthetic fixtures; seed only owned sample projects.
- Contact: paul@draftwright.io.
- Public support: https://github.com/pzfreo/draftwright-claude-plugin/issues.

Before submission, verify login succeeds without Google, MFA, email/SMS codes or
operator approval, and that both drawing/Specify quotas and export permissions are
available. Keep this account and its sample artifacts available for later reviews.
Never paste credentials, bearer URLs or cookies into package files, public issues,
screenshots, result logs or the walkthrough recording.
