---
layout: page
title: linux/grim (español)
description: "Obtiene imágenes (capturas de pantalla) de un compositor Wayland."
content_hash: 8352b2a11d667ca1091263318ab1ff6452a146ba
last_modified_at: 2024-12-01
related_topics:
  - title: English version
    url: /en/linux/grim.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/grim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grim

Obtiene imágenes (capturas de pantalla) de un compositor Wayland.
Más información: <https://sr.ht/~emersion/grim>.

- Hace una captura de pantalla:

`grim`

- Captura de pantalla a un archivo específico:

`grim -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_resultado</span>

- Captura de pantalla de una región específica:

`grim -g "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><posición_x>,<posición_y> <ancho>x<alto></span>`"`

- Selecciona una región específica y toma una captura de dicha porción, usando slurp:

`grim -g "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$(slurp)</span>`"`

- Utiliza un nombre de archivo personalizado:

`grim "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.png</span>`"`

- Captura de pantalla y la copia al portapapeles:

`grim - | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clipboard_manager</span>
