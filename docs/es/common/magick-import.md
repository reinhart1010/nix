---
layout: page
title: common/magick-import (español)
description: "Captura parte o toda la pantalla de un servidor X y guarda la imagen en un archivo."
content_hash: 9810c40f92144464b55dd84d1477dd5b37443bf9
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/magick-import.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/magick-import.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-import.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/magick-import.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># magick import

Captura parte o toda la pantalla de un servidor X y guarda la imagen en un archivo.
Vea también: `magick`.
Más información: <https://imagemagick.org/script/import.php>.

- Captura toda la pantalla del servidor X en un archivo PostScript:

`magick import -window root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.ps</span>

- Captura el contenido de la pantalla de un servidor X remoto en una imagen PNG:

`magick import -window root -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor_remoto</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pantalla</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.png</span>

- Captura una ventana específica dada su ID mostrada por `xwininfo` en una imagen JPEG:

`magick import -window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_ventana</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.jpg</span>
