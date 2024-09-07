---
layout: page
title: common/djxl (español)
description: "Descomprime imágenes JPEG XL."
content_hash: 2562feff9bd640a586762bbada17ceb65c0e1a2c
last_modified_at: 2024-09-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/djxl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># djxl

Descomprime imágenes JPEG XL.
Las extensiones de salida aceptadas son PNG, APNG, JPEG, EXR, PGM, PPM, PNM, PFM, PAM, EXIF, XMP y JUMBF.
Más información: <https://github.com/libjxl/libjxl>.

- Descomprime una imagen JPEG XL a otro formato:

`djxl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.jxl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.ext</span>

- Muestra una página de ayuda muy detallada:

`djxl --help --verbose --verbose --verbose --verbose`
