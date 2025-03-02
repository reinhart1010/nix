---
layout: page
title: windows/es (español)
description: "Interfaz de línea de comandos para Everything, una herramienta de búsqueda rápida de archivos y carpetas para Windows."
content_hash: 75b8eb9dc3c8b890700acc26e2a2cf68ddc39f0c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/windows/es.html
    icon: bi bi-globe
tldri18n_status: 2
---
# es

Interfaz de línea de comandos para Everything, una herramienta de búsqueda rápida de archivos y carpetas para Windows.
Requiere que Everything esté instalado y ejecutándose en segundo plano.
Más información: <https://www.voidtools.com/support/everything/command_line_interface/>.

- Busca un archivo o carpeta por su nombre:

`es `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">término_de_búsqueda</span>

- Busca usando una expresión regular:

`es -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_regex</span>

- Busca palabras completas:

`es -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">término_de_búsqueda</span>

- Limita el número de resultados mostrados:

`es -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">término_de_búsqueda</span>

- Busca dentro de una carpeta específica:

`es -path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta_de_la_carpeta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">término_de_búsqueda</span>

- Lista solo carpetas:

`es /ad`

- Lista solo archivos:

`es /a-d`

- Ordena los resultados (por ejemplo, por nombre):

`es -sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-ascendente</span>
