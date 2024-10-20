---
layout: page
title: linux/btrfs-device (español)
description: "Gestiona dispositivos en un sistema de archivos btrfs."
content_hash: d997761c8ff8b7125abb1735d0946651671ac21c
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs-device.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-device.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs-device.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-device.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-device.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs device

Gestiona dispositivos en un sistema de archivos btrfs.
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- Agrega uno o más dispositivos a un sistema de archivos btrfs:

`sudo btrfs device add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/dispositivo_bloque1</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/dispositivo_bloque2</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_sistema_de_archivos_btrfs</span>

- Elimina un dispositivo de un sistema de archivos btrfs:

`sudo btrfs device remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/dispositivo|id_del_dispositivo</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>`]`

- Muestra estadísticas de errores:

`sudo btrfs device stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_sistema_de_archivos_btrfs</span>

- Escanea todos los discos e informa al kernel de todos los sistemas de archivos btrfs detectados:

`sudo btrfs device scan --all-devices`

- Muestra estadísticas detalladas de asignación por disco:

`sudo btrfs device usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_sistema_de_archivos_btrfs</span>
