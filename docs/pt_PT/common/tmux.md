---
layout: page
title: common/tmux (português (Portugal))
description: "Multiplexador do terminal. Permite várias sessões com janelas, painéis e muito mais."
content_hash: 8e7feefd3d464107eaf7c2b1ed6940904572fdf5
last_modified_at: 2024-01-14
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tmux

Multiplexador do terminal. Permite várias sessões com janelas, painéis e muito mais.
Mais informações: <https://github.com/tmux/tmux>.

- Inicia uma nova sessão:

`tmux`

- Inicia uma sessão com nome:

`tmux new -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Lista sessões existentes:

`tmux ls`

- Entra na última sessão utilizada:

`tmux attach`

- Sai da sessão atual (com o prefixo Ctrl-B):

`<Ctrl>-B d`

- Elimina uma sessão com nome:

`tmux kill-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
