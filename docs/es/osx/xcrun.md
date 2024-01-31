---
layout: page
title: osx/xcrun (español)
description: "Ejecuta o localiza herramientas de desarrollo y propiedades."
content_hash: 797c80dcbafdbee548833df0c50b4a82530b7086
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/xcrun.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcrun

Ejecuta o localiza herramientas de desarrollo y propiedades.
Más información: <https://keith.github.io/xcode-man-pages/xcrun.1.html>.

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
