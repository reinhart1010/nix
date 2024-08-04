---
layout: page
title: common/gdown (español)
description: "Descarga archivos desde Google Drive y otras URLs."
content_hash: a9e379ab8994184e4170e994af756ba23224a296
last_modified_at: 2024-08-04
related_topics:
  - title: English version
    url: /en/common/gdown.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gdown.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gdown

Descarga archivos desde Google Drive y otras URLs.
Más información: <https://github.com/wkentaro/gdown>.

- Descarga un archivo desde una URL:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Descarga usando un ID de archivo:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_archivo</span>

- Descarga con extracción de ID de archivo difuso (también funciona con enlaces <https://docs.google.com>):

`gdown --fuzzy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Descarga una carpeta utilizando su ID o la URL completa:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_carpeta|url</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_de_salida</span>` --folder`

- Descarga un archivo tar, escríbelo en `stdout` y extráelo:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar_url</span>` -O - --quiet | tar xvf -`
