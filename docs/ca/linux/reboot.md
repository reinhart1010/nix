---
layout: page
title: linux/reboot (català)
description: "Reinicia la màquina."
content_hash: 2f8dcfb3c3d8272534ff5c908eaeb55aa45d6335
related_topics:
  - title: English version
    url: /en/linux/reboot.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/reboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
---
# reboot

Reinicia la màquina.
Més informació: <https://www.man7.org/linux/man-pages/man8/reboot.8.html>.

- Reinicia inmediatament:

`reboot`

- Apaga el sistema (el mateix que `poweroff`):

`reboot --poweroff`

- Atura el sistema (el mateix que halt):

`reboot --halt`

- Reinicia inmediatament sense contactar l'adminstrador del sistema:

`reboot --force --force`

- Escriu l'entrada wtmp shutdown sense reiniciar el sistema:

`reboot --wtmp-only`
