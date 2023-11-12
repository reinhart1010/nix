---
layout: page
title: common/rubocop (español)
description: "Analiza archivos de Ruby."
content_hash: 9ef8408b363c29ef8c4e0b3662214495583abd7e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/rubocop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/rubocop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rubocop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rubocop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rubocop

Analiza archivos de Ruby.
Más información: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

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
