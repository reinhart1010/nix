---
layout: page
title: osx/lex (español)
description: "Generador de analizadores léxicos."
content_hash: 469e3afcb5bc438bf55a7de21fcf56eee047e786
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/lex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lex

Generador de analizadores léxicos.
Dada la especificación de un analizador léxico, genera código C implementándolo.
Más información: <https://keith.github.io/xcode-man-pages/lex.1.html>.

- Genera un analizador a partir de un fichero Lex:

`lex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>

- Especifica el fichero de salida:

`lex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>` --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.c</span>

- Compila un archivo C generado por Lex:

`cc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/lex.yy.c</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejecutable</span>
