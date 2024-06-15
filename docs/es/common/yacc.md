---
layout: page
title: common/yacc (español)
description: "Genera un analizador sintáctico LALR (en C) con un archivo de especificación de gramática formal."
content_hash: b21ef721cc2a0b1dd7e29516440e5328bac4553d
last_modified_at: 2024-06-15
related_topics:
  - title: English version
    url: /en/common/yacc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yacc

Genera un analizador sintáctico LALR (en C) con un archivo de especificación de gramática formal.
Vea también: `bison`.
Más información: <https://manned.org/yacc.1p>.

- Crea un fichero `y.tab.c` con el código del analizador en C y compila el fichero de gramática con todas las declaraciones constantes necesarias para los valores. El fichero `y.tab.h` con las declaraciones se crea exclusivamente con la opción `-d`:

`yacc -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_gramática.y</span>

- Compila un fichero de gramática con la descripción del analizador sintáctico y un informe de conflictos generados por ambigüedades en la gramática:

`yacc -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_gramática.y</span>` -v`

- Compila un archivo de gramática, y prefija los nombres de los archivos de salida con un prefijo personalizado en lugar de `y`:

`yacc -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_gramática.y</span>` -v -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo</span>
