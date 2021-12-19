---
layout: page
title: common/tmux (español)
description: "Multiplexa varias consolas virtuales."
content_hash: fb78d70478e219e66c59ce3e7a4a94fd5812c56c
related_topics:
  - title: English version
    url: /en/common/tmux.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tmux.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/tmux.html
    icon: bi bi-globe
---
# tmux

Multiplexa varias consolas virtuales.
Más información: <https://github.com/tmux/tmux>.

- Inicia una nueva sesión de tmux:

`tmux`

- Inicia una nueva sesión de tmux y le asigna un nombre:

`tmux new -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Muestra las sesiones:

`tmux ls`

- Adjunta a una sesión:

`tmux a`

- Adjunta a una sesión con un nombre específico:

`tmux a -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Desconecta de la sesión:

`Ctrl + B, D`

- Elimina una sesión con un nombre específico:

`tmux kill-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Elimina una sesión cuando se adjunta:

`Ctrl + B, x (luego se pulsa 'y' para confirmar que sí)`
