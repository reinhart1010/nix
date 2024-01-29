---
layout: page
title: common/qc (español)
description: "Gestiona y ejecuta fragmentos de comandos almacenados en notas QOwnNotes."
content_hash: 3cd893dbee9e8dd3c4d4e39265648589875ef504
last_modified_at: 2024-01-29
related_topics:
  - title: English version
    url: /en/common/qc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qc

Gestiona y ejecuta fragmentos de comandos almacenados en notas QOwnNotes.
Ve también: `qownnotes`.
Más información: <https://www.qownnotes.org/getting-started/command-line-snippet-manager.html>.

- Configura el gestor de fragmentos, por ejemplo para establecer el token de seguridad de QOwnNotes:

`qc configure`

- Busca e imprime fragmentos de comandos almacenados en tu nota `Commands.md` y en todas tus notas etiquetadas con `commands`:

`qc search`

- Ejecuta un fragmento y muestra el comando antes de ejecutarlo:

`qc exec --command`

- Ejecuta el último fragmento y muestra el comando antes de ejecutarlo:

`qc exec --command --last`

- Cambia entre las carpetas de notas en QOwnNotes:

`qc switch`
