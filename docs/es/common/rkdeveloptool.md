---
layout: page
title: common/rkdeveloptool (español)
description: "Flashea, vacía y gestiona el firmware de arranque en dispositivos informáticos basados en Rockchip."
content_hash: 56b23eb795f0ec6747f56b1f828cbce9939e6dde
last_modified_at: 2024-06-15
related_topics:
  - title: English version
    url: /en/common/rkdeveloptool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rkdeveloptool

Flashea, vacía y gestiona el firmware de arranque en dispositivos informáticos basados en Rockchip.
Necesitará encender el dispositivo en modo Maskrom/Bootrom antes de conectarlo a través del USB.
Algunos subcomandos pueden requerir ser ejecutados como el superusuario.
Más información: <https://github.com/rockchip-linux/rkdeveloptool>.

- [l]ista todos los [d]ispositivos flash conectados basados en Rockchip:

`rkdeveloptool ld`

- Inicializa el dispositivo forzándolo a [d]escargar e instalar el gestor de arranque desde un archivo:

`rkdeveloptool db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/bootloader.bin</span>

- Actualiza un gestor de arranque:

`rkdeveloptool ul `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/bootloader.bin</span>

- Escribe una imagen en una partición flash con formato GPT, especificando el sector de almacenamiento inicial (normalmente `0x0`, alias `0`):

`rkdeveloptool wl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sector_inicial</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.img</span>

- Escribe en la partición flash por su nombre amigable:

`rkdeveloptool wlx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_partición</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.img</span>

- [r]einicia/repón el [d]ispositivo, sal del modo Maskrom/Bootrom para arrancar en la partición flash seleccionada:

`rkdeveloptool rd`
