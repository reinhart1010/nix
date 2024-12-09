---
layout: page
title: linux/xsel (español)
description: "Herramienta X11 de selección y manipulación del portapapeles."
content_hash: ab7cfc02dace5b61aaa25c86dadf3fdc059f1867
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/linux/xsel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/xsel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/xsel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xsel

Herramienta X11 de selección y manipulación del portapapeles.
Más información: <https://manned.org/xsel>.

- Utiliza la salida de un comando como entrada del portapapeles (clip[b]oard) (equivalente a `Ctrl + C`):

`echo 123 | xsel -ib`

- Utiliza el contenido de un archivo como entrada del portapapeles:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` | xsel -ib`

- Envía el contenido del portapapeles a la terminal (equivalente a `Ctrl + V`):

`xsel -ob`

- Envía el contenido del portapapeles a un archivo:

`xsel -ob > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Limpia el portapapeles:

`xsel -cb`

- Envía el contenido de la selección primaria X11 a la terminal (equivalente a clic del tercer botón del ratón):

`xsel -op`
