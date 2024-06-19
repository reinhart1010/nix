---
layout: page
title: osx/shuf (español)
description: "Genera permutaciones aleatorias."
content_hash: 83468009f4698651d1ca8bac37e3aa2c4c3b71c0
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/shuf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/shuf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/shuf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/shuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shuf

Genera permutaciones aleatorias.
Más información: <https://keith.github.io/xcode-man-pages/shuf.1.html>.

- Ordena aleatoriamente las líneas de un fichero y muestra el resultado:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_archivo</span>

- Sólo muestra las 5 primeras entradas del resultado:

`shuf --head-count=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_archivo</span>

- Escribe el resultado en otro archivo:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_archivo</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_archivo_salida</span>

- Genera números aleatorios en el rango 1-10:

`shuf --input-range=1-10`
