---
layout: page
title: common/tmux (français)
description: "Multiplexeur de terminaux. Permet plusieurs sessions avec fenêtres, panneaux, et plus encore."
content_hash: 70af484f04eaba9f21fa9aff036cd5436b9c163a
related_topics:
  - title: English version
    url: /en/common/tmux.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tmux.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/tmux.html
    icon: bi bi-globe
---
# tmux

Multiplexeur de terminaux. Permet plusieurs sessions avec fenêtres, panneaux, et plus encore.
Plus d'informations : <https://github.com/tmux/tmux>.

- Démarrer une nouvelle session :

`tmux`

- Démarrer une nouvelle session nommée :

`tmux new-session -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Lister les sessions existantes :

`tmux ls`

- S'attacher à la session utilisée la plus récemment :

`tmux attach-session`

- S'attacher à une session nommée :

`tmux attach-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Se détacher de la session actuelle (avec le préfixe Ctrl-B) :

`Ctrl-B d`

- Détruire une session nommée :

`tmux kill-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Détruire la session actuelle (avec le préfixe Ctrl-B) :

`Ctrl-B :kill-session<Enter>`
