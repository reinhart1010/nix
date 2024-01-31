---
layout: page
title: osx/mdfind (español)
description: "Lista los archivos que coinciden con una consulta dada."
content_hash: 74ba615c408da2b4c594d776d769d160b370aa2c
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/mdfind.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/mdfind.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mdfind

Lista los archivos que coinciden con una consulta dada.
Más información: <https://keith.github.io/xcode-man-pages/mdfind.1.html>.

- Busca un archivo por su nombre:

`mdfind -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Busca un archivo por su contenido:

`mdfind "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">consulta</span>`"`

- Busca un archivo que contenga una cadena, en un directorio determinado:

`mdfind -onlyin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">consulta</span>`"`
