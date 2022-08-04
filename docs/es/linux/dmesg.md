---
layout: page
title: linux/dmesg (español)
description: "Escribe los mensajes del núcleo a la salida estándar."
content_hash: 2cb67c5bad346138d0ab57edcf544b12985093bf
related_topics:
  - title: English version
    url: /en/linux/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
---
# dmesg

Escribe los mensajes del núcleo a la salida estándar.
Más información: <https://manned.org/dmesg>.

- Muestra los mensajes del núcleo:

`dmesg`

- Muestra los mensajes de error del núcleo:

`dmesg --level err`

- Muestra los mensajes del núcleo y sigue leyedos los nuevos, similar a `tail -f` (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -w`

- Muestra cuanta memoria física hay disponible en este sistema:

`dmesg | grep -i memory`

- Muestra los mensajes del núcleo, página a página:

`dmesg | less`

- Muestra los mensajes del núcleo con una estampilla temporal (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -T`

- Muestra los mensajes del núcleo de forma legible para humanos (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -H`

- Colorea la salida (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -L`
