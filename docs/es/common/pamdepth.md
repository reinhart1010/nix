---
layout: page
title: common/pamdepth (español)
description: "Reduce la profundidad (es decir, la resolución de color) en una imagen."
content_hash: 0b7c8bfbd0f2ef5018b914c5039f32285b8744ac
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/pamdepth.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pamdepth.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamdepth.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamdepth.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamdepth

Reduce la profundidad (es decir, la resolución de color) en una imagen.
Más información: <https://netpbm.sourceforge.net/doc/pamdepth.html>.

- Lee una imagen PBM, fija su valor máximo y la guarda en un archivo:

`pamdepth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_máximo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pbm</span>
