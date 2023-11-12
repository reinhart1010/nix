---
layout: page
title: osx/lipo (español)
description: "Herramienta para el manejo de binarios universales Mach-O."
content_hash: 19252de081c0e4804f7ea708601f57bd369a80dd
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/lipo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lipo

Herramienta para el manejo de binarios universales Mach-O.
Más información: <https://ss64.com/osx/lipo.html>.

- Crea un archivo universal a partir de dos archivos de una sola arquitectura:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo/binario.x86_64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario.arm64e</span>` -create -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario</span>

- Lista todas las arquitecturas contenidas en un archivo universal:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario</span>` -archs`

- Muestra información detallada sobre un archivo universal:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario</span>` -detailed_info`

- Extrae un archivo de arquitectura única de un archivo universal:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario</span>` -thin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arm64e</span>` -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario.arm64e</span>
