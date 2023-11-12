---
layout: page
title: linux/dmesg (español)
description: "Escribe los mensajes del núcleo a la salida estándar."
content_hash: d2698f50dad9fa68fc8b4a5e40063b329c3c4ab2
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/dmesg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmesg.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Escribe los mensajes del núcleo a la salida estándar.
Más información: <https://manned.org/dmesg>.

- Muestra los mensajes del núcleo:

`dmesg`

- Muestra los mensajes de error del núcleo:

`dmesg --level err`

- Muestra los mensajes del núcleo y sigue leyendo los nuevos, similar a `tail -f` (disponible en los núcleos 3.5.0 y posteriores):

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
