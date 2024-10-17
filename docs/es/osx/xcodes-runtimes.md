---
layout: page
title: osx/xcodes-runtimes (español)
description: "Gestiona los tiempos de ejecución de Xcode Simulator."
content_hash: e958b67412690b42a32d3b923b63a30da4a89fbf
last_modified_at: 2024-10-17
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
tldri18n_status: 2
---
# xcodes runtimes

Gestiona los tiempos de ejecución de Xcode Simulator.
Más información: <https://github.com/xcodesorg/xcodes>.

- Muestra todos los tiempos de ejecución del simulador disponibles:

`xcodes runtimes --include-betas`

- Descarga un tiempo de ejecución para el Simulator:

`xcodes runtimes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_tiempo_de_ejecución</span>

- Descarga e instala un tiempo de ejecución para el Simulator:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_tiempo_de_ejecución</span>

- Descarga/instala un tiempo de ejecución del Simulator para una versión específica de iOS/watchOS/tvOS/visionOS (debe escribirse distinguiendo entre mayúsculas y minúsculas):

`xcodes runtimes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">download|install</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iOS|watchOS|tvOS|visionOS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión_de_tiempo_de_ejecución</span>`"`

- Establece una ubicación específica en la que se descargará primero el archivo de tiempo de ejecución (por defecto es `~/Downloads`):

`xcodes runtimes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">download|install</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_tiempo_de_ejecución</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>

- No elimina el archivo descargado cuando el Simulator se instala correctamente:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_tiempo_de_ejecución</span>` --keep-archive`
