---
layout: page
title: linux/halt (English)
description: "Halt the system."
content_hash: 000d4e90bac5d06d22f084a5aeb3a7e48b339761
related_topics:
  - title: español version
    url: /es/linux/halt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/halt.html
    icon: bi bi-globe
---
# halt

Halt the system.
More information: <https://www.man7.org/linux/man-pages/man8/halt.8.html>.

- Halt the system:

`halt`

- Power off the system (same as `poweroff`):

`halt --poweroff`

- Reboot the system (same as `reboot`):

`halt --reboot`

- Halt immediately without contacting the system manager:

`halt --force --force`

- Write the wtmp shutdown entry without halting the system:

`halt --wtmp-only`
