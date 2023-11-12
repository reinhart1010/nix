---
layout: page
title: linux/poweroff (English)
description: "Power off the system."
content_hash: e3198b15af48821e183405a09a27224764a46c60
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/poweroff.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/poweroff.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/poweroff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/poweroff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/poweroff.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/poweroff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# poweroff

Power off the system.
More information: <https://www.man7.org/linux/man-pages/man8/poweroff.8.html>.

- Power off the system:

`poweroff`

- Halt the system (same as `halt`):

`poweroff --halt`

- Reboot the system (same as `reboot`):

`poweroff --reboot`

- Shut down immediately without contacting the system manager:

`poweroff --force --force`

- Write the wtmp shutdown entry without shutting down the system:

`poweroff --wtmp-only`
