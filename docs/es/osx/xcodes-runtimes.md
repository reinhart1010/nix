---
layout: page
title: osx/xcodes-runtimes (español)
description: "Gestiona los tiempos de ejecución de Xcode Simulator."
content_hash: 20b1cbb937c5ca9ef7bfee260212c9c0a78f4377
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/xcodes-runtimes.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xcodes runtimes

Gestiona los tiempos de ejecución de Xcode Simulator.
Más información: <https://github.com/xcodesorg/xcodes>.

- Muestra todos los tiempos de ejecución del simulador disponibles:

`xcodes runtimes --include-betas`

- Descarga un simulador de un tiempo de ejecución:

`xcodes runtimes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_tiempo_de_ejecución</span>

- Descarga e instala un simulador de un tiempo de ejecución:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_tiempo_de_ejecución</span>
