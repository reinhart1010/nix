---
layout: page
title: osx/dot_clean (español)
description: "Fusiona los archivos ._* con los archivos nativos correspondientes."
content_hash: d30f714715c80000da6f14f50b79d3afacaec47f
last_modified_at: 2023-08-03
related_topics:
  - title: English version
    url: /en/osx/dot_clean.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dot_clean.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dot_clean

Fusiona los archivos ._* con los archivos nativos correspondientes.
Más información: <https://ss64.com/osx/dot_clean.html>.

- Fusiona todos los ficheros `._*` recursivamente:

`dot_clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- No fusiona recursivamente todos los `._*` en un directorio (fusión plana):

`dot_clean -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Fusiona y elimina todos los archivos `._*`:

`dot_clean -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Elimina sólo los archivos `._*` si hay un archivo nativo coincidente:

`dot_clean -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Sigue los enlaces simbólicos:

`dot_clean -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Muestra resultados detallados:

`dot_clean -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
