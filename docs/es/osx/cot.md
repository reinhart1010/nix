---
layout: page
title: osx/cot (español)
description: "El editor de texto simple para macOS."
content_hash: b9d1e0b1052000c29ae73e9ff92850ccc63065be
last_modified_at: 2023-07-26
related_topics:
  - title: English version
    url: /en/osx/cot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/cot.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cot

El editor de texto simple para macOS.
Más información: <https://coteditor.com/>.

- Inicia CotEditor:

`cot`

- Abre archivos específicos:

`cot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Abre un nuevo documento en blanco:

`cot --new`

- Abre un archivo específico y bloquea el terminal hasta que se cierre:

`cot --wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre un archivo específico con el cursor en una línea y columna específicas:

`cot --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
