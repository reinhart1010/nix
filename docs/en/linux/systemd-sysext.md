---
layout: page
title: linux/systemd-sysext (English)
description: "Activate or deactivate system extension images."
content_hash: 5330501ef9260231292aa45f8909e5e5217fe686
last_modified_at: 2023-12-06
related_topics:
  - title: Nederlands version
    url: /nl/linux/systemd-sysext.html
    icon: bi bi-globe
tldri18n_status: 2
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

- Refresh system extension images (a combination of `unmerge` and `merge`):

`systemd-sysext refresh`
