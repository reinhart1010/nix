---
layout: page
title: linux/halt (català)
description: "Deté, apaga o reinicia la màquina."
content_hash: b352fc3064711c7d298d84c6f89bd28024d29c66
related_topics:
  - title: English version
    url: /en/linux/halt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/halt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/halt.html
    icon: bi bi-globe
---
# halt

Deté, apaga o reinicia la màquina.
Més informació: <https://www.man7.org/linux/man-pages/man8/halt.8.html>.

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
