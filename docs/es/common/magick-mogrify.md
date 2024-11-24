---
layout: page
title: common/magick-mogrify (español)
description: "Realiza operaciones en múltiples imágenes, como redimensionar, recortar, voltear y añadir efectos."
content_hash: ea6f46b3497e8038aae22eab8b00a792bafc3908
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/magick-mogrify.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/magick-mogrify.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-mogrify.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/magick-mogrify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># magick mogrify

Realiza operaciones en múltiples imágenes, como redimensionar, recortar, voltear y añadir efectos.
Los cambios se aplican directamente al archivo original.
Vea también: `magick`.
Más información: <https://imagemagick.org/script/mogrify.php>.

- Redimensiona todas las imágenes JPEG en el directorio al 50% de su tamaño inicial:

`magick mogrify -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- Redimensiona todas las imágenes comenzando con `DSC` a 800x600:

`magick mogrify -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DSC*</span>

- Convierte todos los PNG a JPEG:

`magick mogrify -format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Redimensiona todas las imágenes JPEG en el directorio al 50% de su tamaño inicial:

`magick mogrify -modulate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100,50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- Dobla el brillo de todos los archivos de imagen en el directorio actual:

`magick mogrify -modulate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- Reduce tamaños de archivos de todas las imágenes GIF en el directorio actual reduciendo la calidad:

`magick mogrify -layers 'optimize' -fuzz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.gif</span>
