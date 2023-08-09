---
layout: page
title: osx/sips (español)
description: "Sistema de procesamiento de imágenes Apple Scriptable."
content_hash: dc07e1d86bfc130bc73227c8b5bf9db1eba5f3f6
last_modified_at: 2023-08-09
related_topics:
  - title: English version
    url: /en/osx/sips.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/sips.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sips

Sistema de procesamiento de imágenes Apple Scriptable.
Imágenes Raster/Query y Perfiles ICC ColorSync.
Más información: <https://ss64.com/osx/sips.html>.

- Especifica un directorio de salida para que los originales no se modifiquen:

`sips --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_salida</span>

- Remuestrea la imagen al tamaño especificado, la relación de aspecto de la imagen puede verse alterada:

`sips --resampleHeightWidth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920}</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_imagen.ext</span>

- Remuestrea la imagen para que la altura y la anchura no superen el tamaño especificado (fíjate en la Z mayúscula):

`sips --resampleHeightWidthMax `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920}</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_imagen.ext</span>

- Remuestrea todas las imágenes de un directorio para que se ajusten a una anchura de 960px (respetando la relación de aspecto):

`sips --resampleWidth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">960</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/imágenes</span>

- Convierte una imagen de CMYK a RGB:

`sips --matchTo "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/imagen.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_salida</span>

- Elimina el perfil ICC ColorSync de una imagen:

`sips --deleteProperty profile --deleteColorManagementProperties `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_imagen.ext</span>
