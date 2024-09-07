---
layout: page
title: common/cjxl (español)
description: "Comprime imágenes a JPEG XL."
content_hash: 82b9b61fa05cc1f5d6b6017462da6276f8798ab3
last_modified_at: 2024-09-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cjxl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cjxl

Comprime imágenes a JPEG XL.
Las extensiones de entrada aceptadas son PNG, APNG, GIF, JPEG, EXR, PPM, PFM, PAM, PGX y JXL.
Más información: <https://github.com/libjxl/libjxl>.

- Convierte una imagen a JPEG XL:

`cjxl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.jxl</span>

- Ajusta la calidad a sin pérdidas y maximiza la compresión de la imagen resultante:

`cjxl --distance 0 --effort 9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.jxl</span>

- Muestra una página de ayuda muy detallada:

`cjxl --help --verbose --verbose --verbose --verbose`
