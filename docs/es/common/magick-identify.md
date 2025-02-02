---
layout: page
title: common/magick-identify (español)
description: "Describe el formato y las características de los archivos de imagen."
content_hash: 6fdb69aa4c55d5dccfa5721338197a81118e1fdf
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/common/magick-identify.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/magick-identify.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-identify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick identify

Describe el formato y las características de los archivos de imagen.
Vea también: `magick`.
Más información: <https://imagemagick.org/script/identify.php>.

- Describe el formato y las características básicas de una imagen:

`magick identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen</span>

- Describe el formato y las características de una imagen detalladamente:

`magick identify -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen</span>

- Recopila las dimensiones de todos los archivos JPEG en el directorio actual y los guarda en un archivo CSV:

`magick identify -format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%f,%w,%h\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.csv</span>
