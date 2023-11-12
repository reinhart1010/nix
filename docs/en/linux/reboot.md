---
layout: page
title: linux/reboot (English)
description: "Reboot the system."
content_hash: a02044e19a18b1544175fcb2c0fcb66cbf57d545
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/reboot.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/reboot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/reboot.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/reboot.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/reboot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/reboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reboot

Reboot the system.
More information: <https://manned.org/reboot.8>.

- Reboot the system:

`reboot`

- Power off the system (same as `poweroff`):

`reboot --poweroff`

- Halt (terminates all processes and shuts down the CPU) the system (same as `halt`):

`reboot --halt`

- Reboot immediately without contacting the system manager:

`reboot --force`

- Write the wtmp shutdown entry without rebooting the system:

`reboot --wtmp-only`
