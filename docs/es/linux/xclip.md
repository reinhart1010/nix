---
layout: page
title: linux/xclip (español)
description: "Herramienta para manipular el portapapeles de X11, similar a `xsel`."
content_hash: 86fc030900a3bfa2078536a8ed6e94fb0f522b9c
last_modified_at: 2024-01-02
related_topics:
  - title: العربية version
    url: /ar/linux/xclip.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/xclip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/xclip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xclip

Herramienta para manipular el portapapeles de X11, similar a `xsel`.
Maneja la selección primaria y secundaria de X y el portapapeles (`Ctrl + C`/`Ctrl + V`).
Más información: <https://manned.org/xclip>.

- Copia la salida de un comando a la selección primaria de X11:

`echo 123 | xclip`

- Copia la salida de un commando a una selección de X11:

`echo 123 | xclip -selection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary|secondary|clipboard</span>

- Copia la salida de un commando al portapapeles, usando notación corta:

`echo 123 | xclip -sel clip`

- Copia el contenido de un fichero al portapapeles:

`xclip -sel clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.txt</span>

- Copia el contenido de un fichero con formato PNG al portapapeles:

`xclip -sel clip -t image/png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.png</span>

- Copia la entrada del usuario al portapapeles:

`xclip -i`

- Imprime el contenido de la selección primaria de X11:

`xclip -o`

- Imprime el contenido del portapapeles:

`xclip -o -sel clip`
