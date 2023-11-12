---
layout: page
title: common/pio-update (English)
description: "Update installed PlatformIO Core packages, development platforms and global libraries."
content_hash: 4fefa48b4fe31b6f681d73e29e145dd90163a832
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pio update

Update installed PlatformIO Core packages, development platforms and global libraries.
See also: `pio platform update`, `pio lib update`.
More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_update.html>.

- Perform a full update of all packages, development platforms and global libraries:

`pio update`

- Update core packages only (skips platforms and libraries):

`pio update --core-packages`

- Check for new versions of packages, platforms and libraries but do not actually update them:

`pio update --dry-run`
