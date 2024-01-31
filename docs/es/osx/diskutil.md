---
layout: page
title: osx/diskutil (español)
description: "Utilidad para gestionar discos y volúmenes locales."
content_hash: db5b0ce3720fe7f65fadb766dfe6df7ec0dd2a05
last_modified_at: 2024-01-31
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
Más información: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- Lista todos los discos, particiones y volúmenes montados actualmente disponibles:

`diskutil list`

- Repara las estructuras de datos del sistema de archivos de un volumen:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device</span>

- Desmonta un volumen:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device</span>

- Expulsa un CD/DVD (primero lo desmonta):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device1</span>
