---
layout: page
title: linux/halt (català)
description: "Deté, apaga o reinicia la màquina."
content_hash: 0c43d7b3926b8475dff7471584e39a3d8b34038e
last_modified_at: 2023-10-03
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

`halt --force --force`

- Escriu l'entrada de wtpm shutdown sense aturar el sistema:

`halt --wtmp-only`
