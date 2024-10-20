---
layout: page
title: linux/btrfs-inspect-internal (español)
description: "Consulta información interna de un sistema de archivos btrfs."
content_hash: 816063398c94b5f4f32ddb12e897fe914ad2e63b
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs inspect-internal

Consulta información interna de un sistema de archivos btrfs.
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- Imprime la información del superbloque:

`sudo btrfs inspect-internal dump-super `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la_partición</span>

- Imprime la información del superbloque y de todas sus copias:

`sudo btrfs inspect-internal dump-super --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la_partición</span>

- Imprime la información de los metadatos del sistema de archivos:

`sudo btrfs inspect-internal dump-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la_partición</span>

- Imprime la lista de archivos en el inodo `n`-ésimo:

`sudo btrfs inspect-internal inode-resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>

- Imprime la lista de archivos en una dirección lógica dada:

`sudo btrfs inspect-internal logical-resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_lógica</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>

- Imprime estadísticas de los árboles de root, extent, csum y fs:

`sudo btrfs inspect-internal tree-stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la_partición</span>
