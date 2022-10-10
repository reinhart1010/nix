---
layout: page
title: linux/reboot (català)
description: "Reinicia la màquina."
content_hash: 9a2607095542a0c2ba3de96fda0382ff9f023fa0
related_topics:
  - title: English version
    url: /en/linux/reboot.html
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
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
---
# reboot

Reinicia la màquina.
Més informació: <https://manned.org/reboot.8>.

- Reinicia inmediatament:

`reboot`

- Apaga el sistema (el mateix que `poweroff`):

`reboot --poweroff`

- Atura el sistema (el mateix que halt):

`reboot --halt`

- Reinicia inmediatament sense contactar l'adminstrador del sistema:

`reboot --force`

- Escriu l'entrada wtmp shutdown sense reiniciar el sistema:

`reboot --wtmp-only`
