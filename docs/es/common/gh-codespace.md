---
layout: page
title: common/gh-codespace (español)
description: "Conecta y gestiona tus codespaces en GitHub."
content_hash: d0d19629bf47a181d8b1664860690b0312cb97b3
last_modified_at: 2024-11-26
related_topics:
  - title: English version
    url: /en/common/gh-codespace.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gh-codespace.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/gh-codespace.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gh-codespace.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-codespace.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh codespace

Conecta y gestiona tus codespaces en GitHub.
Más información: <https://cli.github.com/manual/gh_codespace>.

- Crea un codespace en GitHub de forma interactiva:

`gh codespace create`

- Lista todos los codespaces disponibles:

`gh codespace list`

- Conecta a un codespace vía SSH de forma interactiva:

`gh codespace ssh`

- Transfiere un archivo específico a un codespace interactivamente:

`gh codespace cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_fuente</span>` remote:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_remoto</span>

- Lista los puertos de un codespace interactivo:

`gh codespace ports`

- Muestra los registros (logs) de un codespace interactivo:

`gh codespace logs`

- Elimina un codespace interactivamente:

`gh codespace delete`

- Muestra ayuda para un subcomando:

`gh codespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code|cp|create|delete|edit|...</span>` --help`
