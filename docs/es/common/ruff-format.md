---
layout: page
title: common/ruff-format (español)
description: "Un formador de código Python extremadamente rápido."
content_hash: 74d4e6c939358eb8ed12e69c7567b9d2a8236af4
last_modified_at: 2024-12-26
related_topics:
  - title: English version
    url: /en/common/ruff-format.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ruff-format.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ruff-format.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ruff-format.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ruff format

Un formador de código Python extremadamente rápido.
Si no se especifican archivos o directorios, se utiliza el directorio de trabajo actual de forma predeterminada.
Más información: <https://docs.astral.sh/ruff/formatter>.

- Formatea los archivos o directorios:

`ruff format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...</span>

- Imprime qué archivos habrían sido modificados y devuelve un código de salida no cero si hay archivos a reformatear; y cero de lo contrario:

`ruff format --check`

- Imprime qué cambios se harían sin modificar los archivos:

`ruff format --diff`
