# Product Drive CMS V19 — Bot Reliability Audit

- Default/max video settings added to WhatsApp configuration.
- WhatsApp inbound idempotency claim happens before handler execution, with processing lease and done state.
- Duplicate/concurrent deliveries are ignored safely; failed handlers release the claim.
- WhatsApp Graph API failures are written to system_audit_logs with HTTP status and Meta error identifiers.
- WhatsApp media upload failures are audited.
- Google Drive upload/download failures are audited with operation and HTTP/error context.
- Secrets/tokens are never written to audit context.
- Legacy installations auto-migrate the processed-message table.
