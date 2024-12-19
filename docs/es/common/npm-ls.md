---
layout: page
title: common/npm-ls (español)
description: "Imprime los paquetes instalados a `stdout`."
content_hash: cd5d53d62545bfb22d0d65a90d5cc3205a7c18ec
last_modified_at: 2024-12-19
related_topics:
  - title: English version
    url: /en/common/npm-ls.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/npm-ls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm ls

Imprime los paquetes instalados a `stdout`.
Más información: <https://docs.npmjs.com/cli/commands/npm-ls>.

- Imprime todas las versiones de dependencias directas a `stdout`:

`npm ls`

- Imprime todos los paquetes instalados incluyendo las dependencias de pares:

`npm ls --all`

- Imprime las dependencias con información ampliada:

`npm ls --long`

- Imprime las dependencias en formato parseable:

`npm ls --parseable`

- Imprime dependencias en formato JSON:

`npm ls --json`
