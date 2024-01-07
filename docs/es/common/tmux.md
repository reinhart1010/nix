---
layout: page
title: common/tmux (español)
description: "Multiplexor de terminal."
content_hash: 53da9d0e734108c1dab082087284b18ff7839b30
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/tmux.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tmux.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tmux.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tmux.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/tmux.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tmux

Multiplexor de terminal.
Permite múltiples sesiones con ventanas, paneles y más.
Vea también: `zellij`, `screen`.
Más información: <https://github.com/tmux/tmux>.

- Inicia una nueva sesión:

`tmux`

- Inicia una nueva sesión con nombre:

`tmux new -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Lista las sesiones existentes:

`tmux ls`

- Adjunta a la última sesión utilizada:

`tmux attach`

- Separa la sesión actual (dentro de una sesión tmux):

`<Ctrl>-B d`

- Crea una nueva ventana (dentro de una sesión tmux):

`<Ctrl>-B c`

- Cambia entre sesiones y ventanas (dentro de una sesión tmux):

`<Ctrl>-B w`

- Da de baja una sesión por su nombre:

`tmux kill-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>
