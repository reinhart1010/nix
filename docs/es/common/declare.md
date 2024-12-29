---
layout: page
title: common/declare (español)
description: "Declara variables y les da atributos."
content_hash: e35b19a75257c575d48f076303c008ef342c0352
last_modified_at: 2024-12-29
related_topics:
  - title: English version
    url: /en/common/declare.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/declare.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/declare.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># declare

Declara variables y les da atributos.
Más información: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

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
