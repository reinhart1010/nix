---
layout: page
title: linux/systemd-sysext (English)
description: "Activate or deactivate system extension images."
content_hash: 85dbdbb7a7794749504d57e028c944b15c83f521
last_modified_at: 2023-09-17
---
# systemd-sysext

Activate or deactivate system extension images.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-sysext.html>.

- List installed extension images:

`systemd-sysext list`

- Merge system extension images into `/usr/` and `/opt/`:

`systemd-sysext merge`

- Check the current merge status:

`systemd-sysext status`

- Unmerge all currently installed system extension images from `/usr/` and `/opt/`:

`systemd-sysext unmerge`

- Refresh system extension images (a combination of unmerge and merge):

`systemd-sysext refresh`
