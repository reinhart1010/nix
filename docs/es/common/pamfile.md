---
layout: page
title: common/pamfile (español)
description: "Describe archivos Netpbm (PAM o PNM)."
content_hash: 82a12a567827580dee646c9bac36ecfa6727ec8a
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/pamfile.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pamfile.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamfile.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamfile.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamfile

Describe archivos Netpbm (PAM o PNM).
Más información: <https://netpbm.sourceforge.net/doc/pamfile.html>.

- Describe los archivos Netpbm especificados:

`pamfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Describe cada imagen en cada archivo de entrada (a diferencia de la primera imagen en cada archivo) en un formato legible para la máquina:

`pamfile -allimages -machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra un conteo de cuántas imágenes contiene el archivo:

`pamfile -count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
