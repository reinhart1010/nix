---
layout: page
title: linux/showkey (español)
description: "Muestra el código de las teclas pulsadas en el teclado, útil para depurar problemas relacionados con el teclado y la reasignación de teclas."
content_hash: 818244472ec7e1776884eb9858a0a44ba3ec6e44
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/linux/showkey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# showkey

Muestra el código de las teclas pulsadas en el teclado, útil para depurar problemas relacionados con el teclado y la reasignación de teclas.
Más información: <https://manned.org/showkey>.

- Visualiza códigos de teclas en decimal:

`sudo showkey`

- Visualiza códigos de rastreo en hexadecimal:

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--scancodes</span>

- Muestra códigos de teclas en decimal (por defecto):

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-k|--keycodes</span>

- Muestra los códigos en ASCII, decimal y hexadecimal:

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--ascii</span>

- Sal del programa:

`Ctrl + d`
