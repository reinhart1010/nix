---
layout: page
title: linux/poweroff (español)
description: "Apaga el sistema."
content_hash: 3a2b6d02d5f1d67c37a7ec9a5ac394c9ef03e027
last_modified_at: 2024-07-07
related_topics:
  - title: català version
    url: /ca/linux/poweroff.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/poweroff.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># poweroff

Apaga el sistema.
Más información: <https://www.manned.org/poweroff>.

- Apaga el sistema:

`poweroff`

- Detén el sistema (igual que `halt`):

`poweroff --halt`

- Reinicia el sistema (igual que `reboot`):

`poweroff --reboot`

- Apaga inmediatamente el sistema sin contactar al administrador:

`poweroff --force --force`

- Escribe una entrada en el archivo wtmp sin apagar el sistema:

`poweroff --wtmp-only`
