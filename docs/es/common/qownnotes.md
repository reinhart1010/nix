---
layout: page
title: common/qownnotes (español)
description: "Aplicación de toma de notas en formato Markdown."
content_hash: 7a1bc160f85a813f0beeb25b438b50544d7c715d
last_modified_at: 2024-02-01
related_topics:
  - title: English version
    url: /en/common/qownnotes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qownnotes

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
