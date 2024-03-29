---
layout: page
title: common/tmux (français)
description: "Multiplexeur de terminaux. Permet plusieurs sessions avec fenêtres, panneaux, et plus encore."
content_hash: 885fc14258d9112761e439c54d33e5decaf425b2
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/tmux.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tmux.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tmux

Multiplexeur de terminaux. Permet plusieurs sessions avec fenêtres, panneaux, et plus encore.
Plus d'informations : <https://github.com/tmux/tmux>.

- Démarrer une nouvelle session :

`tmux`

- Démarrer une nouvelle session nommée :

`tmux new -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Lister les sessions existantes :

`tmux ls`

- S'attacher à la session utilisée la plus récemment :

`tmux attach`

- Se détacher de la session actuelle (avec le préfixe Ctrl-B) :

`<Ctrl>-B d`

- Détruire une session nommée :

`tmux kill-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>
