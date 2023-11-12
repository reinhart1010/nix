---
layout: page
title: common/git-switch (français)
description: "Basculez entre les branches Git. Nécessite la version 2.23+ de Git."
content_hash: c1c9e05c5a5f4b58c68fc7a35e307264ad5d0f3e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-switch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-switch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-switch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-switch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-switch.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-switch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git switch

Basculez entre les branches Git. Nécessite la version 2.23+ de Git.
Voir également `git checkout`.
Plus d'informations : <https://git-scm.com/docs/git-switch>.

- Baculer sur une branche existante :

`git switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Créer une nouvelle branche et basculer dessus :

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Créer une nouvelle branche en partant d'un commit donné et basculer dessus :

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Basculer sur la branche précédente :

`git switch -`

- Basculer vers une branche et mettre à jour tous les sous-modules pour qu'ils correspondent :

`git switch --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Basculer vers une branche et fusionner automatiquement la branche actuelle et toutes les modifications non validées dedans :

`git switch --merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>
