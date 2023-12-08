---
layout: page
title: linux/halt (català)
description: "Deté, apaga o reinicia la màquina."
content_hash: 8688760fdf5e8c822fa17e6793cdd430ca3ee0b5
last_modified_at: 2023-12-08
related_topics:
  - title: English version
    url: /en/linux/halt.html
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

Deté, apaga o reinicia la màquina.
Més informació: <https://manned.org/halt.8>.

- Deté la màquina:

`halt`

- Apaga la màquina (el mateix que `poweroff`):

`halt --poweroff`

- Reinicia la màquina (el mateix que `reboot`):

`halt --reboot`

- Deté la màquina inmediatament sense contactar l'administrador de sistemes:

`halt --force`

- Escriu l'entrada de wtpm shutdown sense aturar el sistema:

`halt --wtmp-only`
