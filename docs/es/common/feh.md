---
layout: page
title: common/feh (español)
description: "Utilidad ligera de visualización de imágenes."
content_hash: 4db5b04475010780ea2ee8068859f78bd7f10041
related_topics:
  - title: English version
    url: /en/common/feh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/feh.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># feh

Utilidad ligera de visualización de imágenes.
Más información: <https://feh.finalrewind.org>.

- Muestra imágenes localmente o usando una URL:

`feh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen</span>

- Muestra imágenes recursivamente:

`feh --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Muestra imágenes sin bordes:

`feh --borderless `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen</span>

- Cierra después de la última imagen:

`feh --cycle-once `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen</span>

- Agrega una demora al ciclo de la presentación:

`feh --slideshow-delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secundos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen</span>

- Cambia el fondo de pantalla (centrado, llenar, maximizado, ampliado o amontonado):

`feh --bg-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">center|fill|max|scale|tile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen</span>

- Crea un montage de todas las imágenes en un directorio. Produce una nueva imagen:

`feh --montage --thumb-height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">150</span>` --thumb-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">150</span>` --index-info "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%nn%wx%h</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nueva_imagen</span>
