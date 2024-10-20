---
layout: page
title: linux/btrfs-subvolume (español)
description: "Gestiona subvolúmenes e imágenes instantáneas de btrfs."
content_hash: 4049747fec30e4cf3f84f137151918e2a192d1fa
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-subvolume.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs subvolume

Gestiona subvolúmenes e imágenes instantáneas de btrfs.
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- Crea un nuevo subvolumen vacío:

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/nuevo_subvolumen</span>

- Lista todos los subvolúmenes e imágenes instantáneas en el sistema de archivos especificado:

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_sistema_de_archivos_btrfs</span>

- Elimina un subvolumen:

`sudo btrfs subvolume delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_subvolumen</span>

- Crea una imagen instantánea de solo lectura de un subvolumen existente:

`sudo btrfs subvolume snapshot -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_subvolumen_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_destino</span>

- Crea una imagen instantánea de lectura y escritura de un subvolumen existente:

`sudo btrfs subvolume snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_subvolumen_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_destino</span>

- Muestra información detallada sobre un subvolumen:

`sudo btrfs subvolume show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_subvolumen</span>
