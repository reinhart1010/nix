---
layout: page
title: linux/halt (español)
description: "Detiene, apaga o reinicia la máquina."
content_hash: 5f0258aeba8eade45922b462520cac698e98c15e
last_modified_at: 2024-10-24
related_topics:
  - title: català version
    url: /ca/linux/halt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/halt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/halt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/halt.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># halt

Detiene, apaga o reinicia la máquina.
Ver también: `poweroff`, `reboot`.
Más información: <https://manned.org/halt.8>.

- Detiene el sistema:

`halt`

- Apaga el sistema (igual que `poweroff`):

`halt --poweroff`

- Reinicia el sistema (igual que `reboot`):

`halt --reboot`

- Apaga inmediatamente el sistema sin contactar al administrador:

`halt --force`

- Escribe la entrada de apagado en wtmp sin apagar el sistema:

`halt --wtmp-only`
