---
layout: page
title: common/latexpand (español)
description: "Simplifica los archivos fuente LaTeX eliminando comentarios y resolviendo `\include`s, `\input`s, etc."
content_hash: 450373fd9b2b85f26efa48f3c6719b43a1f453f6
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/latexpand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# latexpand

Simplifica los archivos fuente LaTeX eliminando comentarios y resolviendo `\include`s, `\input`s, etc.
Más información: <https://www.ctan.org/pkg/latexpand>.

- Simplifica el archivo fuente dado y guarda el resultado en el archivo de salida especificado:

`latexpand --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.tex</span>

- No elimina los comentarios:

`latexpand --keep-comments --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.tex</span>

- No expande `\include`s, `\input`s etc.:

`latexpand --keep-includes --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.tex</span>

- Expande `\usepackage`s hasta encontrar los archivos STY correspondientes:

`latexpand --expand-usepackage --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.tex</span>

- Incorpora el archivo BBL especificado:

`latexpand --expand-bbl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/bibliografía.bbl</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.tex</span>
