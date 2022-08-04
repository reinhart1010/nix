---
layout: page
title: common/vimdiff (español)
description: "Abre dos o más archivos en Vim y muestra las diferencias entre ellos."
content_hash: 5e3db3c5a9080293a2e7aa6210de6b4ddd4b8ae0
related_topics:
  - title: English version
    url: /en/common/vimdiff.html
    icon: bi bi-globe
---
# vimdiff

Abre dos o más archivos en Vim y muestra las diferencias entre ellos.
Ver también `vim`.
Más información: <https://www.vim.org>.

- Abre dos archivos y muestra las diferencias:

`vimdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo2</span>

- Mueve el cursor a la ventana de la izquierda|derecha:

`Ctrl + w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h|l</span>

- Salta a la siguiente diferencia:

`[c`

- Salta a la diferencia previa:

`]c`

- Copia la diferencia resaltada de la otra ventana a la ventana actual:

`do`

- Copia la diferencia resaltada de la ventana actual a la otra ventana:

`dp`

- Actualiza todos los resaltados y folds (plegados de texto):

`:diffupdate`

- Alterna la apertura/cierre de la fold (plegado de texto) de código resaltada:

`za`
