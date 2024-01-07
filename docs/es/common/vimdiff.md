---
layout: page
title: common/vimdiff (español)
description: "Abre dos o más archivos en Vim y muestra las diferencias entre ellos."
content_hash: f7d2fab8382b6c13ac9b203e1223f780bda28d2c
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/common/vimdiff.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vimdiff.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vimdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vimdiff

Abre dos o más archivos en Vim y muestra las diferencias entre ellos.
Vea también `vim`.
Más información: <https://www.vim.org>.

- Abre dos archivos y muestra las diferencias:

`vimdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo2</span>

- Mueve el cursor a la ventana de la izquierda|derecha:

`<Ctrl> + w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h|l</span>

- Salta a la diferencia previa:

`[c`

- Salta a la siguiente diferencia:

`]c`

- Copia la diferencia resaltada de la otra ventana a la ventana actual:

`do`

- Copia la diferencia resaltada de la ventana actual a la otra ventana:

`dp`

- Actualiza todos los resaltados y folds (plegados de texto):

`:diffupdate`

- Alterna la apertura/cierre de la fold (plegado de texto) de código resaltada:

`za`
