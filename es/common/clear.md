---
layout: page
title: common/clear (español)
description: "Limpia la pantalla de la terminal."
content_hash: 884bf63783a868aef19f40a5e765814ce946ee69
related_topics:
  - title: Deutsch version
    url: /de/common/clear.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clear.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/clear.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/clear.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clear.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clear.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clear.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/clear.html
    icon: bi bi-globe
---
# clear

Limpia la pantalla de la terminal.
Más información: <https://manned.org/clear>.

- Limpia la pantalla de la terminal (equivale a presionar Control-L en la interfaz de línea de comandos Bash):

`clear`

- Limpia la pantalla pero mantiene el buffer de desplazamiento:

`clear -x`

- Indica el tipo de terminal a limpiar (por defecto se utiliza el valor de la variable de entorno `TERM`):

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_de_terminal</span>

- Muestra la versión de `ncurses` utilizada por `clear`:

`clear -V`
