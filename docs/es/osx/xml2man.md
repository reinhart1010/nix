---
layout: page
title: osx/xml2man (español)
description: "Compila MPGL a mdoc."
content_hash: 3b5300c7672164a6c3fdad068a92feac3d8a088c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/xml2man.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xml2man

Compila MPGL a mdoc.
Más información: <https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html>.

- Compila un archivo MPGL a una página man visible:

`xml2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_comando.mxml</span>

- Compila un archivo MPGL a un archivo de salida específico:

`xml2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_servicio.mxml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_servicio.7</span>

- Compila un archivo MPGL a un archivo de salida específico, sobrescribiéndolo si ya existe:

`xml2man -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_funcion.mxml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_funcion.3</span>
