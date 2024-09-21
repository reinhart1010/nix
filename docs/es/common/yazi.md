---
layout: page
title: common/yazi (español)
description: "Rápido gestor de archivos escrito en Rust."
content_hash: bde680d43a8543542ecfb54592183a0bc8866d66
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/yazi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yazi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yazi

Rápido gestor de archivos escrito en Rust.
Experiencia de gestión de archivos eficiente, fácil de usar y personalizable.
Más información: <https://github.com/sxyazi/yazi>.

- Inicia Yazi desde el directorio actual:

`yazi`

- Imprime información de depuración:

`yazi --debug`

- Escribe el directorio de trabajo actual al salir del archivo:

`yazi --cwd-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_cwd</span>

- Borra el directorio de caché:

`yazi --clear-cache`
