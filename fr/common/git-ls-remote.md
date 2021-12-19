---
layout: page
title: common/git-ls-remote (français)
description: "Commande Git pour répertorier les références dans un dépôt distant en fonction du nom ou de l'URL."
content_hash: 373aec3dd95cb0ebb75e4f5587abcc9eb2deb51f
related_topics:
  - title: English version
    url: /en/common/git-ls-remote.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-ls-remote.html
    icon: bi bi-globe
---
# git ls-remote

Commande Git pour répertorier les références dans un dépôt distant en fonction du nom ou de l'URL.
Si aucun nom ou URL n'est donné, alors la branche amont configurée sera utilisée, ou l'origine distante si la première n'est pas configurée.
Plus d'informations : <https://git-scm.com/docs/git-ls-remote>.

- Afficher les références du dépôt configuré par défaut :

`git ls-remote`

- Afficher uniquement les références HEAD du dépôt configuré par défaut :

`git ls-remote --heads`

- Afficher uniquement les tags du dépôt configuré par défaut :

`git ls-remote --tags`

- Afficher les références du dépôt précisé :

`git ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url-du-dépôt</span>

- Afficher les références du dépôt précisé filtrés par un motif :

`git ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom-du-dépôt</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif</span>`"`
