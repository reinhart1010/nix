---
layout: page
title: linux/ydotool (español)
description: "Controla las entradas de teclado y ratón mediante comandos de forma agnóstica al servidor de visualización."
content_hash: b2e7ef3f1477c4de64928594b72804e71bca55dd
last_modified_at: 2024-04-09
related_topics:
  - title: English version
    url: /en/linux/ydotool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ydotool

Controla las entradas de teclado y ratón mediante comandos de forma agnóstica al servidor de visualización.
Más información: <https://github.com/ReimuNotMoe/ydotool>.

- Inicia el daemon ydotool en segundo plano:

`ydotoold`

- Realiza un clic con el botón izquierdo:

`ydotool click 0xC0`

- Realiza un clic con el botón derecho:

`ydotool click 0xC1`

- Ingresa la combinación de teclas Alt+F4:

`ydotool key 56:1 62:1 62:0 56:0`
