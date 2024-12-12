---
layout: page
title: common/tex-fmt (español)
description: "Formatea el código fuente LaTeX."
content_hash: c7ebd2e9f5d2eb40c053cec03fd5fd5ca28f6237
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/common/tex-fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tex-fmt

Formatea el código fuente LaTeX.
Más información: <https://github.com/WGUNDERWOOD/tex-fmt>.

- Formatea un archivo, sobrescribiendo el original:

`tex-fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.tex</span>

- Comprueba si un archivo está formateado correctamente:

`tex-fmt --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.tex</span>

- Formatea un archivo leído de `stdin` y lo imprime en `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.tex</span>` | tex-fmt --stdin`
