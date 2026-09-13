# Product Drive CMS V20 — WhatsApp Reliability Audit

Applied fixes:
- Atomic WhatsApp message idempotency claim: active processing locks are never stolen; only insert winner or expired lock can claim.
- WhatsApp Graph API outbound requests retry up to 3 times for network/408/425/429/5xx failures with backoff.
- Webhook signature and invalid JSON failures are written to System Audit with safe metadata; secrets are never logged.
- WhatsApp media metadata/binary download failures are audited with HTTP status and safe error metadata.
- Removed duplicate/unsafe message delete handling and added audit on delete failure.
- `wa_configured()` and Settings status now require App Secret as well as Verify Token, Access Token, and Phone Number ID.
- Existing V18/V19 features retained: App Secret persistence, Greeting template, video defaults/max, Drive sync counters, and detailed API audit.

Validation:
- All PHP files lint successfully.
