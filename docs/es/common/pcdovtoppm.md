---
layout: page
title: common/pcdovtoppm (español)
description: "Crea una imagen índice para un CD de fotos basándose en su archivo de resumen."
content_hash: a7e5fde49578f60669e01ed68b30e0e492cb7208
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pcdovtoppm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pcdovtoppm

Crea una imagen índice para un CD de fotos basándose en su archivo de resumen.
Más información: <https://netpbm.sourceforge.net/doc/pcdovtoppm.html>.

- Crea una imagen índice PPM a partir de un archivo de vista general PCD:

`pcdovtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.ppm</span>

- Especifica la anchura [m]áxima de la imagen de salida y el tamaño máximo de cada una de las imágenes contenidas en la salida:

`pcdovtoppm -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anchura</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tamaño</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.ppm</span>

- Especifica el número máximo de imágenes y el número máximo de [c]olores:

`pcdovtoppm -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_imágenes</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colores</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida.ppm</span>

- Utiliza la [f]uente especificada para las anotaciones y pinta el fondo blanco:

`pcdovtoppm -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fuente</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.ppm</span>
