---
layout: page
title: common/bmptopnm (español)
description: "Convierte un archivo BMP a una imagen PBM, PGM o PNM."
content_hash: 1db2e39c9b1e9e3fc9897b09ceaa007140f0971d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/bmptopnm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bmptopnm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bmptopnm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bmptopnm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bmptopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bmptopnm

Convierte un archivo BMP a una imagen PBM, PGM o PNM.
Más información: <https://netpbm.sourceforge.net/doc/bmptopnm.html>.

- Genera la imagen PBM, PGM o PNM como salida; para Windows y OS/2 únicamente procesa BMP:

`bmptopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bmp</span>

- Reporta la información del encabezado BMP a `stderr`:

`bmptopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bmp</span>

- Muestra la versión:

`bmptopnm -version`
