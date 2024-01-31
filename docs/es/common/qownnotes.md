---
layout: page
title: common/qownnotes (español)
description: "Aplicación de toma de notas en formato Markdown."
content_hash: 7a1bc160f85a813f0beeb25b438b50544d7c715d
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/common/qownnotes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qownnotes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qownnotes

Aplicación de toma de notas en formato Markdown.
Se integra opcionalmente con las aplicaciones de toma de notas de Nextcloud y ownCloud.
Vea también: `qc`, para gestionar fragmentos de comandos.
Más información: <https://www.qownnotes.org/getting-started/cli-parameters.html>.

- Ejecuta en modo portable:

`QOwnNotes --portable`

- Muestra la configuración y cualquier otra información sobre la aplicación y su entorno en formato GitHub Markdown:

`QOwnNotes --dump-settings`

- Especifica un contexto diferente para la configuración y los archivos internos:

`QOwnNotes --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prueba</span>

- Activa una acción de menú después de iniciar la aplicación:

`QOwnNotes --action `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">actionShow_Todo_List</span>
