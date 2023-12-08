---
layout: page
title: linux/halt (English)
description: "Halt the system."
content_hash: 2c607d4bc492cf6b4b7839c17732c69a7895bb69
last_modified_at: 2023-12-08
related_topics:
  - title: català version
    url: /ca/linux/halt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/halt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/halt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/halt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# halt

Halt the system.
More information: <https://manned.org/halt.8>.

- Halt the system:

`halt`

- Power off the system (same as `poweroff`):

`halt --poweroff`

- Reboot the system (same as `reboot`):

`halt --reboot`

- Halt immediately without contacting the system manager:

`halt --force`

- Write the wtmp shutdown entry without halting the system:

`halt --wtmp-only`
