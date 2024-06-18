---
layout: page
title: osx/xcrun (español)
description: "Ejecuta o localiza herramientas de desarrollo y propiedades."
content_hash: e086ba2a07740f128375f8ef3157b753fe32636e
last_modified_at: 2024-06-18
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

- Busca una herramienta para un SDK:

`xcrun --sdk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_sdk</span>

- Busca una herramienta para una cadena de herramientas:

`xcrun --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_cadena</span>

- Muestra ayuda:

`xcrun --help`

- Muestra la versión:

`xcrun --version`
