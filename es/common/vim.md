---
layout: page
title: common/vim (español)
description: "Vim (Vi IMproved), un editor de texto para la línea de comandos, que proporciona varios modos para diferentes tipos de manipulación de texto."
content_hash: 8360e5cf0e923ca83c85f94538a6406d61cc120d
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
---
# vim

Vim (Vi IMproved), un editor de texto para la línea de comandos, que proporciona varios modos para diferentes tipos de manipulación de texto.
Pulsando `i` entra en el modo insertar. `<Esc>` regresa al modo normal, permitiendo el uso de comandos Vim.
Más información: <https://www.vim.org>.

- Abre un archivo:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre un archivo en un número de línea especificado:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_línea</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Ver el manual de Vim:

`:help<Enter>`

- Guarda y sale:

`:wq<Enter>`

- Deshace la última operación:

`u`

- Busca un patrón en el archivo (pulsa `n`/`N` para ir a la próxima/previa coincidencia):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_a_buscar</span>`<Enter>`

- Realiza una sustitución de una expresión regular en el archivo completo:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión_regular</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reemplazo</span>`/g<Enter>`

- Muestra los números de línea:

`:set nu<Enter>`
