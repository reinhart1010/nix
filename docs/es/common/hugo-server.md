---
layout: page
title: common/hugo-server (español)
description: "Construye y publica un sitio con el servidor web integrado de Hugo."
content_hash: f11a3c3bf24005c95017451228715dee24e9e32d
last_modified_at: 2024-11-30
related_topics:
  - title: English version
    url: /en/common/hugo-server.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/hugo-server.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hugo server

Construye y publica un sitio con el servidor web integrado de Hugo.
Más información: <https://gohugo.io/commands/hugo_server/>.

- Construye y publica un sitio:

`hugo server`

- Construye y publica un sitio en un número de puerto especificado:

`hugo server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_puerto</span>

- Construye y publica un sitio mientras se minimizan los formatos de salida soportados (HTML, XML, etc.):

`hugo server --minify`

- Construye y sirve un sitio en el entorno de producción con reconstrucción completa (re-render) disminuyendo el tamaño (minify) en los formatos soportados:

`hugo server --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">producción</span>` --disableFastRender --minify`

- Muestra la ayuda:

`hugo server --help`
