# Product Drive CMS — Full Consolidated Build

This repository is consolidated from the latest V20 bot reliability build.

## Included
- Premium SaaS dashboard UI
- Consistent sidebar/topbar and normal typography
- Products, categories, media gallery and preview
- Admin/User roles; User is view/download only
- Google Drive OAuth/sync
- WhatsApp Cloud API webhook
- Greeting template
- Default/max photo and video settings
- Upload sessions and bulk media handling
- Emergency stop
- App Secret signature verification (fail-closed)
- App Secret preservation when settings are saved blank
- Atomic webhook idempotency
- Retry for transient WhatsApp API failures
- Detailed WhatsApp/Drive error audit without secrets
- System Audit/Error Log

## Security
Never commit `.env`, access tokens, App Secrets, or OAuth credentials.
Configure production secrets outside Git.
