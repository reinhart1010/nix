---
layout: page
title: osx/sed (español)
description: "Edita texto de manera programable."
content_hash: 26ef20aca69a26d7fc57bd197e341dd59738fb75
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/sed.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Edita texto de manera programable.
Ver también: `awk`, `ed`.
Más información: <https://keith.github.io/xcode-man-pages/sed.1.html>.

- Reemplaza todas las veces que aparece `apple` (regex básico) por `mango` (regex básico) en todas las líneas de entrada e imprime el resultado en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed 's/apple/mango/g'`

- Ejecuta un script [f] específico e imprime el resultado en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_script.sed</span>

- Sustituye todas las apariciones de `manzana` (regex extendido) por `MANZANA` (regex extendido) en todas las líneas de entrada e imprime el resultado en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -E 's/(manzana)/\U\1/g'`

- Imprime solo la primera línea en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -n '1p'`

- Sustituye todas las apariciones de `manzana` (regex básico) por `mango` (regex básico) en un `fichero` y guarda una copia de seguridad del original en `fichero.bak`:

`sed -i bak 's/manzana/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
