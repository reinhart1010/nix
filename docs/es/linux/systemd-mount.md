---
layout: page
title: linux/systemd-mount (español)
description: "Establece y destruye puntos de montaje transitorio o de montaje automático (auto-mount point)."
content_hash: 60ecd3361832e859be34aa8ea26d3f083f456219
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/systemd-mount.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/systemd-mount.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/systemd-mount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-mount

Establece y destruye puntos de montaje transitorio o de montaje automático (auto-mount point).
Más información: <https://www.freedesktop.org/software/systemd/man/systemd-mount.html>.

- Monta un sistema de archivos (imagen o dispositivo de bloque (block device)) en `/run/media/system/ETIQUETA` donde ETIQUETA es la etiqueta del sistema de archivos o el nombre del dispositivo si no hay etiqueta:

`systemd-mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_dispositivo</span>

- Monta un sistema de archivos (imagen o dispositivo de bloque) en una ubicación específica:

`systemd-mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_dispositivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/punto_de_montaje</span>

- Lista todos los dispositivos locales de bloque conocidos con sistemas de archivos que pueden montarse:

`systemd-mount --list`

- Crea un punto de montaje automático que monta el sistema de archivos al momento del primer acceso:

`systemd-mount --automount=yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_dispositivo</span>

- Desmonta uno o más dispositivos:

`systemd-mount --umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/punto_de_montaje_o_dispositivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/punto_de_montaje_o_dispositivo2</span>

- Monta un sistema de archivos (dispositivo de imagen o bloque) con un tipo de sistema de archivos específico:

`systemd-mount --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_system_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_dispositivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/punto_de_montaje</span>

- Monta un sistema de archivos (imagen o dispositivo de bloque) con opciones adicionales de montaje:

`systemd-mount --options=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opciones_de_montaje</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_dispositivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/punto_de_montaje</span>
