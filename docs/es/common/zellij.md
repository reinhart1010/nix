---
layout: page
title: common/zellij (español)
description: "Multiplexor de terminal con baterías incluidas."
content_hash: 89fed37a21ce97ab0355ef085793b675b673b0b8
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/zellij.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zellij.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zellij

Multiplexor de terminal con baterías incluidas.
Vea también `tmux` y `screen`.
Más información: <https://zellij.dev/documentation/>.

- Inicia una nueva sesión con nombre:

`zellij --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Lista las sesiones existentes:

`zellij list-sessions`

- Abre la sesión más recientemente usada:

`zellij attach`

- Abre un nuevo panel (estando en una sesión de zellij):

`<Alt> + N`

- Desvincula la sesión en curso (estando en una sesión de zellij):

`<Ctrl> + O, D`
