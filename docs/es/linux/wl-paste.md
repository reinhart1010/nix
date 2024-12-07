---
layout: page
title: linux/wl-paste (español)
description: "Pega contenido en el portapapeles Wayland."
content_hash: 273f274b0f8e67afc2d3ea118026533759b50a76
last_modified_at: 2024-12-07
related_topics:
  - title: English version
    url: /en/linux/wl-paste.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/wl-paste.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/wl-paste.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wl-paste.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wl-paste

Pega contenido en el portapapeles Wayland.
Vea también: `wl-copy`, `xclip`.
Más información: <https://github.com/bugaevc/wl-clipboard>.

- Pega el contenido del portapapeles:

`wl-paste`

- Pega el contenido del portapapeles primario (texto seleccionado):

`wl-paste --primary`

- Escribe el contenido del portapapeles a un archivo:

`wl-paste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Envía el contenido del portapapeles a un comando:

`wl-paste | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
