---
layout: page
title: netbsd/sed (español)
description: "Edita texto de manera programable."
content_hash: 4a2bd15e1f0acc0e14718d7c4bef3df0ea42b406
last_modified_at: 2024-02-13
related_topics:
  - title: English version
    url: /en/netbsd/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Edita texto de manera programable.
Vea también: `awk`, `ed`.
Más información: <https://man.netbsd.org/sed.1>.

- Reemplaza todas las ocurrencias de `apple` (expresión regular básica) por `mango` (expresión regular básica) en todas las líneas de entrada e imprime el resultado en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed 's/apple/mango/g'`

- Ejecuta un [f]ichero con un script e imprime el resultado en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.sed</span>

- Retrasa abrir cada archivo hasta que se aplique a una línea de entrada un comando que contenga la función `w` u otra similar:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.sed</span>

- Activa la extensión de GNU de expresiones re[g]ulares:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.sed</span>

- Sustituye todas las ocurrencias de `apple` (expresión regular extendida) por `APPLE` (expresión regular extendida) en todas las líneas de entrada e imprime el resultado en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -E 's/(apple)/\U\1/g'`

- Imprime solo la primera línea en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -n '1p'`

- Sustituye todas las apariciones de `apple` (expresión regular básica) por `mango` (expresión regular básica) en un archivo específico y sobrescribe el archivo original en su lugar:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
