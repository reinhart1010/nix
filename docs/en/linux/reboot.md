---
layout: page
title: linux/reboot (English)
description: "Reboot the system."
content_hash: f8a500dce0815ed9db8298c07fec330defc308dc
related_topics:
  - title: español version
    url: /es/linux/reboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
---
# reboot

Reboot the system.
More information: <https://www.man7.org/linux/man-pages/man8/reboot.8.html>.

- Reboot the system:

`reboot`

- Power off the system (same as `poweroff`):

`reboot --poweroff`

- Halt the system (same as `halt`):

`reboot --halt`

- Reboot immediately without contacting the system manager:

`reboot --force --force`

- Write the wtmp shutdown entry without rebooting the system:

`reboot --wtmp-only`
