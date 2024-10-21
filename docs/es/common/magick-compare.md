---
layout: page
title: common/magick-compare (español)
description: "Crea una imagen de comparación para anotar visualmente la diferencia entre dos imágenes."
content_hash: cf0d243fb3e6c4e737a338a86c09dd5dbf1b1a55
last_modified_at: 2024-10-21
related_topics:
  - title: Deutsch version
    url: /de/common/magick-compare.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/magick-compare.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/magick-compare.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/magick-compare.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/magick-compare.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-compare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick compare

Crea una imagen de comparación para anotar visualmente la diferencia entre dos imágenes.
Vea también: `magick`.
Más información: <https://imagemagick.org/script/compare.php>.

- Compara dos imágenes:

`magick compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/diff.png</span>

- Compara dos imágenes usando una métrica específica:

`magick compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/diff.png</span>
