---
layout: page
title: linux/dmesg (català)
description: "Escriu els missatges del kernel a la sortida estàndar."
content_hash: 63bc46b6aafafa2c561099685c97c7160b1f5376
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/linux/dmesg.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmesg.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Escriu els missatges del kernel a la sortida estàndar.
Més informació: <https://manned.org/dmesg>.

- Mostra els missatges del kernel:

`sudo dmesg`

- Mostra els missatges d'error del kernel:

`sudo dmesg --level err`

- Mostra els missatges del kernel i segueix llegint els nous, similar a `tail -f` (disponible en kernels 3.5.0 i posteriors):

`sudo dmesg -w`

- Mostra quanta memòria física hi ha disponible en el sistema:

`sudo dmesg | grep -i memory`

- Mostra tots els missatges del kernel, pàgina a pàgina:

`sudo dmesg | less`

- Mostra els missatges del kernel amb una estampa temporal (disponible en kernels 3.5.0 i posteriors):

`sudo dmesg -T`

- Mostra els missatges del kernel de forma llegible per humans (disponible en kernels 3.5.0 i posteriors):

`sudo dmesg -H`

- Pinta la sortida (disponible en kernels 3.5.0 i posteriors):

`sudo dmesg -L`
