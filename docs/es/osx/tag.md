---
layout: page
title: osx/tag (español)
description: "Edita etiquetas en archivos de Mac OS X (10.9 Mavericks y superior)."
content_hash: 3e941e54d79206cbdb9dfc427370017d0a49e27b
last_modified_at: 2024-12-18
related_topics:
  - title: English version
    url: /en/osx/tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tag

Edita etiquetas en archivos de Mac OS X (10.9 Mavericks y superior).
Más información: <https://github.com/jdberry/tag/>.

- Añade etiquetas a un archivo:

`tag --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_etiqueta1,nombre_etiqueta2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Elimina una etiqueta:

`tag --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_etiqueta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Elimina todas las etiquetas de un archivo:

`tag --remove \* `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra todos los archivos con una etiqueta determinada:

`tag --match `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>
