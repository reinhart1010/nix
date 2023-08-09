---
layout: page
title: osx/xcrun (español)
description: "Ejecuta o localiza herramientas de desarrollo y propiedades."
content_hash: 928f99e2ec98799f1a367a7ba585c0c7ed2aadb6
last_modified_at: 2023-08-09
related_topics:
  - title: English version
    url: /en/osx/xcrun.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xcrun

Ejecuta o localiza herramientas de desarrollo y propiedades.
Más información: <https://www.unix.com/man-page/osx/1/xcrun/>.

- Localiza y ejecuta una herramienta desde el directorio activo de desarrolladores:

`xcrun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">herramienta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>

- Muestra resultados detallados:

`xcrun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">herramienta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>` --verbose`

- Busca una herramienta para un SDK determinado:

`xcrun --sdk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_sdk</span>

- Busca una herramienta para una cadena de herramientas determinada:

`xcrun --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Muestra versión:

`xcrun --version`

- Muestra ayuda:

`xcrun --help`
