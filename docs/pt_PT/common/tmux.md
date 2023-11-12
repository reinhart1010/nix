---
layout: page
title: common/tmux (português (Portugal))
description: "Multiplexador do terminal. Permite várias sessões com janelas, painéis e muito mais."
content_hash: 2e4ff1a64513b0393f44b3de7883d36f50e015e9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/tmux.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tmux.html
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
tldri18n_status: 2
---
# tmux

Multiplexador do terminal. Permite várias sessões com janelas, painéis e muito mais.
Mais informações: <https://github.com/tmux/tmux>.

- Iniciar uma nova sessão:

`tmux`

- Iniciar uma sessão com nome:

`tmux new-session -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Listar sessões existentes:

`tmux ls`

- Entrar na última sessão utilizada:

`tmux attach-session`

- Entrar numa sessão com nome:

`tmux attach-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Sair da sessão atual (com o prefixo Ctrl-B):

`Ctrl-B d`

- Eliminar uma sessão com nome:

`tmux kill-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Eliminar a sessão atual (com o prefixo Ctrl-B):

`Ctrl-B :kill-session<Enter>`
