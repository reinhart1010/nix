---
layout: page
title: osx/mdfind (español)
description: "Lista los archivos que coinciden con una consulta dada."
content_hash: 8e5406ac2397bbd5418b0e10ca4c81bf74fa3adc
last_modified_at: 2023-09-13
related_topics:
  - title: English version
    url: /en/osx/mdfind.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/mdfind.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mdfind

Lista los archivos que coinciden con una consulta dada.
Más información: <https://ss64.com/osx/mdfind.html>.

- Busca un archivo por su nombre:

`mdfind -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Busca un archivo por su contenido:

`mdfind "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">consulta</span>`"`

- Busca un archivo que contenga una cadena, en un directorio determinado:

`mdfind -onlyin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">consulta</span>`"`
