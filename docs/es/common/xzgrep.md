---
layout: page
title: common/xzgrep (español)
description: "Busca archivos posiblemente comprimidos con `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, o `zstd` utilizando expresiones regulares."
content_hash: 4f68129237ebba734fcd30841e14cf20fab54f6e
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/xzgrep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/xzgrep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xzgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xzgrep

Busca archivos posiblemente comprimidos con `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, o `zstd` utilizando expresiones regulares.
Vea también: `grep`.
Más información: <https://manned.org/xzgrep>.

- Busca un patrón dentro de un archivo:

`xzgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Busca una cadena exacta (sin expresiones regulares):

`xzgrep --fixed-strings "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_exacta</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Busca un patrón en todos los archivos mostrando los números de línea que coinciden:

`xzgrep --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Utiliza expresiones regulares extendidas (soporta `?`, `+`, `{}`, `()` y `|`), sin diferenciar mayúsculas y minúsculas (case-insensitive):

`xzgrep --extended-regexp --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime 3 líneas de contexto alrededor, antes o después de cada coincidencia:

`xzgrep --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context|before-context|after-context</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime el nombre del archivo y número de línea para cada coincidencia en color:

`xzgrep --with-filename --line-number --color=always "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Busca líneas que coincidan con un patrón, imprime solo el texto coincidente:

`xzgrep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
