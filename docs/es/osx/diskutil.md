---
layout: page
title: osx/diskutil (español)
description: "Utilidad para gestionar discos y volúmenes locales."
content_hash: 6d29df84dcc1c8ebb8438d2f155c0338484e464d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/diskutil.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/diskutil.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/diskutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/diskutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/diskutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diskutil

Utilidad para gestionar discos y volúmenes locales.
Más información: <https://ss64.com/osx/diskutil.html>.

- Lista todos los discos, particiones y volúmenes montados actualmente disponibles:

`diskutil list`

- Repara las estructuras de datos del sistema de archivos de un volumen:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device</span>

- Desmonta un volumen:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device</span>

- Expulsa un CD/DVD (primero lo desmonta):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device1</span>
