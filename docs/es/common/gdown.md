---
layout: page
title: common/gdown (español)
description: "Descarga archivos desde Google Drive y otras URLs."
content_hash: a9e379ab8994184e4170e994af756ba23224a296
last_modified_at: 2024-08-05
related_topics:
  - title: English version
    url: /en/common/gdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdown

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
