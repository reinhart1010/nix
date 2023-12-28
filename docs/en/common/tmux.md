---
layout: page
title: common/tmux (English)
description: "Terminal multiplexer."
content_hash: cd3cd832a0392b22f1b4efa0ab444c2735f0a413
last_modified_at: 2023-12-28
related_topics:
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
  - title: português (Portugal) version
    url: /pt_PT/common/tmux.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tmux

Terminal multiplexer.
It allows multiple sessions with windows, panes, and more.
See also: `zellij`, `screen`.
More information: <https://github.com/tmux/tmux>.

- Start a new session:

`tmux`

- Start a new named session:

`tmux new -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List existing sessions:

`tmux ls`

- Attach to the most recently used session:

`tmux attach`

- Detach from the current session (inside a tmux session):

`Ctrl-B d`

- Create a new window (inside a tmux session):

`Ctrl-B c`

- Switch between sessions and windows (inside a tmux session):

`Ctrl-B w`

- Kill a session by name:

`tmux kill-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
