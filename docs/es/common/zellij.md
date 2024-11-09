---
layout: page
title: common/zellij (español)
description: "Multiplexor de terminal con baterías incluidas."
content_hash: 89fed37a21ce97ab0355ef085793b675b673b0b8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/zellij.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zellij.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zellij.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zellij

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
