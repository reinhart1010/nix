---
layout: page
title: common/asciitopgm (español)
description: "Convierte gráficos ASCII hacia un archivo PGM."
content_hash: 622a6e601d64eedc7e12f5591b39fb526aff9ca7
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/asciitopgm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/asciitopgm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciitopgm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/asciitopgm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># asciitopgm

Convierte gráficos ASCII hacia un archivo PGM.
Más información: <https://netpbm.sourceforge.net/doc/asciitopgm.html>.

- Lee los datos ASCII como entrada y produce una imagen PGM con valores de píxel aproximando al "brillo" de los caracteres ASCII:

`asciitopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_entrada</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida.pgm</span>

- Muestra la versión:

`asciitopgm -version`
