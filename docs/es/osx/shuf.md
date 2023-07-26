---
layout: page
title: osx/shuf (español)
description: "Genera permutaciones aleatorias."
content_hash: 13a10a89788a97ce3cdd04d4863327fd0fc6f47b
last_modified_at: 2023-07-26
related_topics:
  - title: English version
    url: /en/osx/shuf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/shuf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/shuf.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># shuf

Genera permutaciones aleatorias.
Más información: <https://www.unix.com/man-page/linux/1/shuf/>.

- Ordena aleatoriamente las líneas de un fichero y muestra el resultado:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_archivo</span>

- Sólo muestra las 5 primeras entradas del resultado:

`shuf --head-count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_archivo</span>

- Escribe el resultado en otro archivo:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_archivo</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_archivo_salida</span>

- Genera números aleatorios en el rango 1-10:

`shuf --input-range=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>
