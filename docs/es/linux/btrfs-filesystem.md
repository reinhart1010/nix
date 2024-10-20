---
layout: page
title: linux/btrfs-filesystem (español)
description: "Gestiona sistemas de archivos btrfs."
content_hash: 3ca571ba83191c96b97ce4b7a0b7c72cd3f25595
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-filesystem.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs filesystem

Gestiona sistemas de archivos btrfs.
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- Muestra el uso del sistema de archivos (de manera opcional ejecutarlo como root para mostrar información detallada):

`btrfs filesystem usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>

- Muestra el uso por dispositivos individuales:

`sudo btrfs filesystem show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>

- Desfragmenta un único archivo en un sistema de archivos btrfs (evita mientras un agente de deduplicación esté en ejecución):

`sudo btrfs filesystem defragment -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Desfragmenta un directorio recursivamente (no cruza los límites de subvolúmenes):

`sudo btrfs filesystem defragment -v -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Fuerza la sincronización de bloques de datos no escritos en disco(s):

`sudo btrfs filesystem sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>

- Resume el uso del disco para los archivos en un directorio de manera recursiva:

`sudo btrfs filesystem du --summarize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
