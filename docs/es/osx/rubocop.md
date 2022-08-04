---
layout: page
title: osx/rubocop (español)
description: "Analiza archivos de Ruby."
content_hash: c02a19d8d4de8bd4d4b11bd0b28fae76be67d92b
related_topics:
  - title: English version
    url: /en/osx/rubocop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/rubocop.html
    icon: bi bi-globe
---
# rubocop

Analiza archivos de Ruby.

- Verifica todos los archivos en el directorio actual (incluyendo subdirectorios):

`rubocop`

- Verifica uno o más archivos o directorios determinados:

`rubocop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Guarda la salida en un archivo:

`rubocop --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Muestra la lista de cops (reglas de análisis):

`rubocop --show-cops`

- Excluye una regla:

`rubocop --except `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_2</span>

- Ejecuta sólo determinadas reglas:

`rubocop --only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_2</span>

- Autocorrige archivos (experimental):

`rubocop --auto-correct`
