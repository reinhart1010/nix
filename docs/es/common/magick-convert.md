---
layout: page
title: common/magick-convert (español)
description: "Convierte entre formatos de imagen, escala, une y crea imágenes."
content_hash: aab453826a7e3f02be561ea6cfa002bc11e8173b
last_modified_at: 2024-10-21
related_topics:
  - title: Deutsch version
    url: /de/common/magick-convert.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/magick-convert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/magick-convert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/magick-convert.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/magick-convert.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-convert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/magick-convert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick convert

Convierte entre formatos de imagen, escala, une y crea imágenes.
Nota: esta herramienta (anteriormente `convert`) ha sido reemplazada por `magick` en ImageMagick 7+.
Más información: <https://imagemagick.org/script/convert.php>.

- Convierte una imagen de JPEG a PNG:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_entrada.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_salida.png</span>

- Escala una imagen al 50% de su tamaño original:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_entrada.png</span>` -resize 50% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_salida.png</span>

- Escala una imagen manteniendo la relación de aspecto original a un tamaño máximo de 640x480:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_entrada.png</span>` -resize 640x480 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_salida.png</span>

- Escala una imagen para tener un tamaño de archivo específico:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_entrada.png</span>` -define jpeg:extent=512kb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_salida.jpg</span>

- Anexa imágenes verticalmente/horizontalmente:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen1.png ruta/a/imagen2.png ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-append|+append</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_salida.png</span>

- Crea un GIF a partir de una serie de imágenes con un retraso de 100ms entre ellas:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen1.png ruta/a/imagen2.png ...</span>` -delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/animacion.gif</span>

- Crea una imagen con solo un fondo rojo sólido:

`magick convert -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` "xc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#ff0000</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.png</span>

- Crea un favicon a partir de varias imágenes de diferentes tamaños:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen1.png ruta/a/imagen2.png ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/favicon.ico</span>
