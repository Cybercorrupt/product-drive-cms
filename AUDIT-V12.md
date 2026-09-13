# Product Drive CMS V12 Audit / V13 preparation

## Fixed in this build

1. **Upload command flow** — `UPLOAD/UNGGAH KODE` is handled before photo/download/lookup paths. A bare product-code lookup no longer silently creates an upload session.
2. **Upload target count** — `UPLOAD P00123 3` starts a 3-photo session; the session closes automatically after the third successful upload. `UPLOAD P00123` remains unlimited until `STOP`.
3. **Existing database migration** — `whatsapp_sessions` now receives `target_count` and `received_count` automatically when the WhatsApp code runs. Fresh schema includes both columns.
4. **Photo send failures** — failed/missing local media and failed Meta sends are counted and reported instead of being silently ignored.
5. **Emergency stop** — checks remain before each photo upload/send operation and before sending the next image.
6. **Failed upload cleanup** — local file is removed if the upload transaction fails before completion.
7. **Login/install CSRF** — POST forms now validate the application CSRF token. Installer also validates email/password server-side.
8. **Runtime dependencies** — `ext-fileinfo` and `ext-zip` are declared because MIME detection and ZIP generation use them.

## Behavior to verify manually after deployment

- `P005597` => product information only; no upload session.
- `UPLOAD P005597` => upload mode, unlimited until `STOP`.
- `UPLOAD P005597 3` => upload mode with exactly 3 successful photos, then automatic completion.
- `STOP` => cancels upload session without changing photo-send emergency status.
- `STOPFOTO` => blocks photo sending for that WhatsApp number.
- `RESUMEFOTO` => re-enables photo sending for that number.
- CMS `STOP ALL PHOTOS` => blocks all photo sending.
- CMS Resume => re-enables all photo sending.
- `FOTO P005597 3` => sends up to 3 images with no captions.
- Duplicate Meta webhook message IDs => processed only once.
