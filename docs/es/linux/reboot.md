---
layout: page
title: linux/reboot (español)
description: "Reinicia el sistema."
content_hash: 0522e4e3d8f80b11494348d3265f6ab2ba983d97
last_modified_at: 2024-10-31
related_topics:
  - title: català version
    url: /ca/linux/reboot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/reboot.html
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
  - title: Nederlands version
    url: /nl/linux/reboot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/reboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reboot

Reinicia el sistema.
Vea también: `halt`, `poweroff`.
Más información: <https://manned.org/reboot.8>.

- Reinicia inmediatamente:

`reboot`

- Apaga el sistema (igual que `poweroff`):

`reboot --poweroff`

- Detiene (termina todos los procesos y apaga la CPU) el sistema (igual que `halt`):

`reboot --halt`

- Reinicia inmediatamente sin contactar al administrador del sistema:

`reboot --force`

- Escribe la entrada wtmp de apagado sin reiniciar el sistema:

`reboot --wtmp-only`
