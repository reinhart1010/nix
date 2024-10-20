---
layout: page
title: linux/btrfs-property (español)
description: "Obtiene, establece o lista propiedades para un objeto de sistema de archivos BTRFS (archivos, directorios, subvolúmenes, sistemas de archivos o dispositivos)."
content_hash: 2db252c12a406cee4cfce0eaf7fef29431c24def
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs-property.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs-property.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-property.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs property

Obtiene, establece o lista propiedades para un objeto de sistema de archivos BTRFS (archivos, directorios, subvolúmenes, sistemas de archivos o dispositivos).
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-property.html>.

- Lista las propiedades disponibles (y descripciones) para el objeto btrfs dado:

`sudo btrfs property list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_objeto_btrfs</span>

- Obtiene todas las propiedades para el objeto btrfs dado:

`sudo btrfs property get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_objeto_btrfs</span>

- Obtiene la propiedad `label` para el sistema de archivos o dispositivo btrfs dado:

`sudo btrfs property get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_sistema_de_archivos_btrfs</span>` label`

- Obtiene todas las propiedades específicas del tipo de objeto para el sistema de archivos o dispositivo btrfs dado:

`sudo btrfs property get -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subvol|filesystem|inode|device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_sistema_de_archivos_btrfs</span>

- Establece la propiedad `compression` para un inodo btrfs dado (ya sea un archivo o un directorio):

`sudo btrfs property set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_inodo_btrfs</span>` compression `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zstd|zlib|lzo|none</span>
