---
layout: page
title: osx/dot_clean (español)
description: "Fusiona los archivos ._* con los archivos nativos correspondientes."
content_hash: a3ea6440ab1eac9610a0cf206795bb7da1baabee
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/dot_clean.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dot_clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dot_clean

Fusiona los archivos ._* con los archivos nativos correspondientes.
Más información: <https://keith.github.io/xcode-man-pages/dot_clean.1.html>.

- Fusiona todos los ficheros `._*` recursivamente:

`dot_clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Fusiona todos los `._*` en un directorio sin leer subdirectorios (fusión plana):

`dot_clean -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Fusiona y elimina todos los archivos `._*`:

`dot_clean -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Elimina sólo los archivos `._*` si hay un archivo nativo coincidente:

`dot_clean -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Sigue los enlaces simbólicos:

`dot_clean -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Muestra resultados detallados:

`dot_clean -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
