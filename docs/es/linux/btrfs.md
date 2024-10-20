---
layout: page
title: linux/btrfs (español)
description: "Un sistema de archivos basado en el principio de copia en escritura (COW) para Linux."
content_hash: b665e0d079ed252dc7399053a271decde712407e
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/btrfs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs

Un sistema de archivos basado en el principio de copia en escritura (COW) para Linux.
Algunos subcomandos como `device` tienen su propia documentación de uso.
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Muestra subvolumen:

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/subvolumen</span>

- Lista subvolúmenes:

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/punto_de_montaje</span>

- Muestra información sobre el uso del espacio:

`sudo btrfs filesystem df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/punto_de_montaje</span>

- Habilita cuota:

`sudo btrfs quota enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/subvolumen</span>

- Muestra cuota:

`sudo btrfs qgroup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/subvolumen</span>
