---
layout: page
title: common/strings (español)
description: "Encuentra cadenas imprimibles en un archivo objeto o binario."
content_hash: 2afd2254049e799d1ba7f848567f79e35426a50f
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/common/strings.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/strings.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/strings.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/strings.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/strings.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/strings.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># strings

Encuentra cadenas imprimibles en un archivo objeto o binario.
Más información: <https://manned.org/strings>.

- Imprime todas las cadenas contenidas en un binario:

`strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Limita resultados a cadenas por lo menos n caracteres de largo:

`strings -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Precede cada resultado con su distancia hasta el inicio (offset) del archivo:

`strings -t d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Precede cada resultado con su desplazamiento (offset) dentro del archivo en hexadecimal:

`strings -t x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
