---
layout: page
title: common/zig (español)
description: "El compilador Zig y la cadena de herramientas."
content_hash: dd02aa959def49b5ecfb2da4153a26e27c7b5da5
last_modified_at: 2024-12-30
related_topics:
  - title: English version
    url: /en/common/zig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zig

El compilador Zig y la cadena de herramientas.
Más información: <https://ziglang.org>.

- Compila el proyecto en el directorio actual:

`zig build`

- Compila y ejecuta el proyecto en el directorio actual:

`zig build run`

- Inicializa un proyecto `zig build` con biblioteca y ejecutable:

`zig init`

- Crea y ejecuta una compilación de pruebas:

`zig test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.zig</span>

- Hace compilación cruzada, arma y ejecuta un proyecto para la arquitectura `x86_64` y el sistema operativo `windows`:

`zig build run -fwine -Dtarget=x86_64-windows`

- Reformatea código fuente Zig en forma canónica:

`zig fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.zig</span>

- Traduce un archivo C a `zig`:

`zig translate-c -lc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.c</span>

- Usa Zig como compilador de C++:

`zig c++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.cpp</span>
