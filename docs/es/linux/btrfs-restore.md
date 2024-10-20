---
layout: page
title: linux/btrfs-restore (español)
description: "Intenta recuperar archivos de un sistema de archivos btrfs dañado."
content_hash: 156182e9e33e007566b9129c912b5b1ecb3f7b65
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs-restore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-restore.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs-restore.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-restore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs restore

Intenta recuperar archivos de un sistema de archivos btrfs dañado.
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Restaura todos los archivos de un sistema de archivos btrfs a un directorio dado:

`sudo btrfs restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_dispositivo_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_directorio_destino</span>

- Lista (sin escribir) los archivos que se van a restaurar de un sistema de archivos btrfs:

`sudo btrfs restore --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_dispositivo_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_directorio_destino</span>

- Restaura archivos que coincidan con una expresión regular dada (insensible a mayúsculas) de un sistema de archivos btrfs (todos los directorios padres de los archivos de destino también deben coincidir):

`sudo btrfs restore --path-regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_dispositivo_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_directorio_destino</span>

- Restaura archivos de un sistema de archivos btrfs usando un `bytenr` específico del árbol raíz (ver `btrfs-find-root`):

`sudo btrfs restore -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bytenr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_dispositivo_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_directorio_destino</span>

- Restaura archivos de un sistema de archivos btrfs (junto con metadatos, atributos extendidos y enlaces simbólicos), sobrescribiendo archivos en el destino:

`sudo btrfs restore --metadata --xattr --symlinks --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_dispositivo_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_directorio_destino</span>
