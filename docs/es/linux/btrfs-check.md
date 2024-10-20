---
layout: page
title: linux/btrfs-check (español)
description: "Verifica o repara un sistema de archivos btrfs."
content_hash: d846139b8916f98277d8b65febf2287b10bda291
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs-check.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-check.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs-check.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-check.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs check

Verifica o repara un sistema de archivos btrfs.
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- Verifica un sistema de archivos btrfs:

`sudo btrfs check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/partición</span>

- Verifica y repara un sistema de archivos btrfs (peligroso):

`sudo btrfs check --repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/partición</span>

- Muestra el progreso de la verificación:

`sudo btrfs check --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/partición</span>

- Verifica la suma de comprobación de cada bloque de datos (si el sistema de archivos es bueno):

`sudo btrfs check --check-data-csum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/partición</span>

- Utiliza el superblock `n`-ésimo (`n` puede ser 0, 1 o 2):

`sudo btrfs check --super `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/partición</span>

- Reconstruye el árbol de suma de comprobación:

`sudo btrfs check --repair --init-csum-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/partición</span>

- Reconstruye el árbol de extensiones:

`sudo btrfs check --repair --init-extent-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/partición</span>
