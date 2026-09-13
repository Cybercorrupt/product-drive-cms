# Audit V18

- App Secret webhook signature verification is strict: missing secret/signature is rejected.
- Saving WhatsApp settings preserves the existing App Secret when the field is blank.
- Added editable `greeting` WhatsApp reply template and greeting keyword handling.
- Added per-session Drive sync success/failure counters and accurate completion summary states.
- Fresh installs include the new Drive counters in `database/schema.sql`; existing installs auto-migrate `whatsapp_sessions`.
- Full PHP lint performed after update.
