---
layout: page
title: common/git-revert (français)
description: "Créer un nouveau commit qui efface les changements du précédent."
content_hash: 1d4a3cf76ef7239aef0f2c1cac8ee372de73f7de
related_topics:
  - title: English version
    url: /en/common/git-revert.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-revert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-revert.html
    icon: bi bi-globe
---
# git revert

Créer un nouveau commit qui efface les changements du précédent.
Plus d'informations : <https://git-scm.com/docs/git-revert>.

- Crée un commit qui annule les changements du dernier commit :

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Crée un commit qui annule les changements des 5 dernier commit :

`git revert HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Crée un commit qui annule les changements de plusieurs commit :

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master~5..master~2</span>

- Ne pas créer de nouveau commit, remplacer uniquement dans l'arbre courant :

`git revert -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9..9a1743</span>
