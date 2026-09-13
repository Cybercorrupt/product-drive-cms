Product Drive CMS V23 - Products CRUD



## Category Management
Categories are stored in the `categories` table. Existing non-empty product categories are migrated automatically on first page load. Admins can create, rename, and delete unused categories. The Add Product form uses the saved categories as a dropdown and allows creating a new category inline.

## Latest UI Update
- Sidebar background is exactly #0f479f.
- Primary buttons use exactly #0f479f.
- Primary button hover/active uses #ee7c13.
- Removed gradient from sidebar and primary buttons.


## BOT REPLY TEMPLATES
Edit all bot text responses from Settings -> WhatsApp -> Template Balasan Bot.
Changes are stored in the app_settings table and are applied by the single V17 webhook handler without editing PHP.

## V17 WhatsApp safety fixes
- Bare product lookup no longer silently enables upload mode.
- Added `upload KODE JUMLAH` with automatic session completion.
- Added upload-session counters with migration for existing databases.
- Added photo-send failure summary and stronger emergency-stop checks.
- Added fail-closed message deduplication and immediate webhook acknowledgement to prevent duplicate photo sends when Meta retries a slow webhook.
- Added cleanup for failed local upload writes.


## V19
Bulk/multi-photo WhatsApp uploads are supported. Use `UPLOAD P005597 6` and send six images. Concurrent image webhook requests are serialized per WhatsApp number instead of being dropped.
