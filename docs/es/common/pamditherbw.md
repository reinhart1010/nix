---
layout: page
title: common/pamditherbw (español)
description: "Aplica dithering a una imagen en escala de grises, es decir, la convierte en un patrón de píxeles blancos y negros que parecen iguales a la escala de grises original."
content_hash: bb8eaecac1febae4d405a11ba0c7c930d10a10c3
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/pamditherbw.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pamditherbw.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamditherbw.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamditherbw.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamditherbw

Aplica dithering a una imagen en escala de grises, es decir, la convierte en un patrón de píxeles blancos y negros que parecen iguales a la escala de grises original.
Vea también: `pbmreduce`.
Más información: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- Lee una imagen PGM, aplica la separación y la guarda en un archivo:

`ppmditherbw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pgm</span>

- Utiliza el método de cuantización especificado:

`ppmditherbw -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">floyd|fs|atkinson|threshold|hilbert|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pgm</span>

- Utiliza el método de cuantización de atkinson y la semilla especificada para un generador de número pseudo-aleatorio:

`ppmditherbw -atkinson -randomseed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1337</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pgm</span>

- Especifica el valor de umbralización (thresholding) para los métodos de cuantización que realizan algún tipo de umbralización:

`ppmditherbw -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fs|atkinson|thresholding</span>` -value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pgm</span>
