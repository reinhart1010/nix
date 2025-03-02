---
layout: page
title: common/readarray (español)
description: "Lee líneas de `stdin` en un arreglo."
content_hash: c7b010273174a4589abb18a6359e300388961ea6
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/readarray.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/readarray.html
    icon: bi bi-globe
tldri18n_status: 2
---
# readarray

Lee líneas de `stdin` en un arreglo.
Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>.

- Ingresa líneas en un arreglo de forma interactiva:

`readarray `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_arreglo</span>

- Lee líneas de un archivo y las inserta en un arreglo:

`readarray `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_arreglo</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.txt</span>

- Elimina los delimitadores finales (newline por defecto):

`readarray -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_arreglo</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.txt</span>

- Copia como máximo el número de líneas especificado:

`readarray -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_arreglo</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.txt</span>
