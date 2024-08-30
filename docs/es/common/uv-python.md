---
layout: page
title: common/uv-python (español)
description: "Gestiona las versiones e instalaciones de Python."
content_hash: f98095faf3518d8cca99991c7f591b1b0e4e9ae4
last_modified_at: 2024-08-30
related_topics:
  - title: English version
    url: /en/common/uv-python.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uv-python.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uv python

Gestiona las versiones e instalaciones de Python.
Más información: <https://docs.astral.sh/uv/reference/cli/#uv-python>.

- Lista todas las instalaciones de Python disponibles:

`uv python list`

- Instala una versión de Python:

`uv python install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Desinstala una versión de Python:

`uv python uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Busca una instalación de Python:

`uv python find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Fija el proyecto actual para utilizar una versión específica de Python:

`uv python pin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Muestra el directorio de instalación de `uv` Python:

`uv python dir`
