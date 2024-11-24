---
layout: page
title: linux/fatrace (español)
description: "Informa de eventos de acceso a archivos."
content_hash: 7b02353cffd3cc7b322f8629a3cbae2d89b39377
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/linux/fatrace.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/fatrace.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fatrace.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fatrace

Informa de eventos de acceso a archivos.
Más información: <https://manned.org/fatrace>.

- Imprime en `stdout` los eventos de acceso a archivos en todos los sistemas de archivos montados:

`sudo fatrace`

- Imprime en `stdout` eventos de acceso a archivos en el montaje del directorio actual, con marcas de tiempo:

`sudo fatrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--current-mount</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--timestamp</span>
