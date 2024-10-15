---
layout: page
title: common/ctags (español)
description: "Genera un archivo de índice (o etiqueta) de objetos de lenguaje que se encuentran en los archivos de código fuente de muchos lenguajes de programación populares."
content_hash: 11f9cf27bee40552fb673b466e032eae734feb37
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/ctags.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ctags.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ctags

Genera un archivo de índice (o etiqueta) de objetos de lenguaje que se encuentran en los archivos de código fuente de muchos lenguajes de programación populares.
Más información: <https://ctags.io/>.

- Genera etiquetas para un solo archivo y las envía a un archivo llamado "tags" en el directorio actual, sobrescribiendo el archivo si existe:

`ctags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Genera etiquetas para todos los archivos en el directorio actual y las envía a un archivo específico, sobrescribiendo el archivo si existe:

`ctags -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` *`

- Genera etiquetas para todos los archivos en el directorio actual y todos los subdirectorios:

`ctags --recurse`

- Genera etiquetas para un solo archivo y las envía con el número de línea inicial y el número de línea final en formato JSON:

`ctags --fields=+ne --output-format=json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
