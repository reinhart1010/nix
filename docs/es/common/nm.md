---
layout: page
title: common/nm (español)
description: "Lista los nombres de símbolos en los archivos objeto."
content_hash: 1a5251baf38da4695d36b08012f1a6b5b223f836
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/nm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nm

Lista los nombres de símbolos en los archivos objeto.
Más información: <https://manned.org/nm>.

- Lista de funciones globales (externas) en un archivo (con prefijo T):

`nm -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.o</span>

- Lista solo los símbolos no definidos en un archivo:

`nm -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.o</span>

- Lista todos los símbolos, incluso símbolos de depuración:

`nm -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.o</span>

- Reconstruye símbolos C++ (hace que sean legibles):

`nm --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.o</span>
