---
layout: page
title: common/autopep8 (español)
description: "Formatea el código Python según la guía de estilo PEP 8."
content_hash: 25facfe8e3d4f774f4ff1684c306a74e85811cac
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/autopep8.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autopep8.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/autopep8.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autopep8

Formatea el código Python según la guía de estilo PEP 8.
Más información: <https://github.com/hhatto/autopep8>.

- Formatea un archivo a `stdout`, con una longitud de línea máxima personalizada:

`autopep8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.py</span>` --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">length</span>

- Formatea un fichero, mostrando un diff de los cambios:

`autopep8 --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Formatea un fichero en su lugar y guarda los cambios:

`autopep8 --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.py</span>

- Formatea recursivamente todos los archivos de un directorio y guarda los cambios:

`autopep8 --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
