---
layout: page
title: common/tmux (português (Portugal))
description: "Multiplexador do terminal. Permite várias sessões com janelas, painéis e muito mais."
content_hash: b30af0507fd2a4bf3dbe3df2fc0b779a6523422e
last_modified_at: 2023-12-28
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

- Inicia uma nova sessão:

`tmux`

- Inicia uma sessão com nome:

`tmux new-session -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Lista sessões existentes:

`tmux ls`

- Entra na última sessão utilizada:

`tmux attach-session`

- Entra numa sessão com nome:

`tmux attach-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Sai da sessão atual (com o prefixo Ctrl-B):

`Ctrl-B d`

- Elimina uma sessão com nome:

`tmux kill-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Elimina a sessão atual (com o prefixo Ctrl-B):

`Ctrl-B :kill-session<Enter>`
