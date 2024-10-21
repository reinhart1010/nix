---
layout: page
title: common/magick-montage (español)
description: "Coloca imágenes en una cuadrícula personalizable."
content_hash: beaf4add62e4201e22ae0794d20d5820dd74cff2
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/magick-montage.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/magick-montage.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-montage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick montage

Coloca imágenes en una cuadrícula personalizable.
Vea también: `magick`.
Más información: <https://imagemagick.org/script/montage.php>.

- Coloca imágenes en una cuadrícula, redimensionando automáticamente las imágenes más grandes que el tamaño de la celda de la cuadrícula:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen1.jpg ruta/a/imagen2.jpg ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/montaje.jpg</span>

- Coloca imágenes en una cuadrícula, calculando automáticamente el tamaño de la celda de la cuadrícula a partir de la imagen más grande:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen1.jpg ruta/a/imagen2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0+0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/montaje.jpg</span>

- Especifica el tamaño de la celda de la cuadrícula y redimensiona las imágenes para ajustarlas antes de colocarlas en la cuadrícula:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen1.jpg ruta/a/imagen2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480+0+0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/montaje.jpg</span>

- Limita el número de filas y columnas en la cuadrícula, causando que las imágenes de entrada desborden en múltiples montajes de salida:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen1.jpg ruta/a/imagen2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0+0</span>` -tile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2x3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">montaje_%d.jpg</span>

- Redimensiona y recorta las imágenes para llenar sus celdas de cuadrícula antes de colocarlas:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen1.jpg ruta/a/imagen2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0+0</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480^</span>` -gravity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">center</span>` -crop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480+0+0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/montaje.jpg</span>
