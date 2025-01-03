---
layout: page
title: common/declare (español)
description: "Declara variables y les da atributos."
content_hash: 2dd20313c55bfd95bb0ae1be49982b848d4d74be
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/common/declare.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/declare.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/declare.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># declare

Declara variables y les da atributos.
Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-declare>.

- Describe una variable de cadena con el valor especificado:

`declare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`"`

- Declara una variable entera con el valor especificado:

`declare -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`"`

- Describe una variable arreglo con el valor especificado:

`declare -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_a item_b item_c</span>`)`

- Declara una variable arreglo asociativo con el valor especificado:

`declare -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[key_a]=item_a [key_b]=item_b [key_c]=item_c</span>`)`

- Declara una variable de cadena de solo lectura con el valor especificado:

`declare -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`"`

- Declara una variable global dentro de una función con el valor especificado:

`declare -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`"`
