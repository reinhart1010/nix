---
layout: page
title: common/magick (español)
description: "Crea, edita, compone o convierte entre formatos de imagen."
content_hash: 854ab44afafbad6c3b8104af924506536929ba76
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/magick.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/magick.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/magick.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># magick

Crea, edita, compone o convierte entre formatos de imagen.
Esta herramienta reemplaza a `convert` en ImageMagick 7+. Usa `magick convert` para utilizar la herramienta antigua en versiones 7+.
Algunos subcomandos, como `mogrify`, tienen su propia documentación de uso.
Más información: <https://imagemagick.org>.

- Convierte entre formatos de imagen:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_entrada.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_salida.jpg</span>

- Redimensiona una imagen, creando una nueva copia:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_entrada.jpg</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100x100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_salida.jpg</span>

- Crea un GIF a partir de todas las imágenes JPEG en el directorio actual:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagenes.gif</span>

- Crea un patrón de tablero de ajedrez:

`magick -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480</span>` pattern:checkerboard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/tablero.png</span>

- Crea un archivo PDF a partir de todas las imágenes JPEG en el directorio actual:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -adjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo.pdf</span>
