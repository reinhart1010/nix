---
layout: page
title: common/git-checkout (français)
description: "Extraire une branche ou des chemins vers l'arborescence de travail."
content_hash: 56662ba57f8fca26a0181ce273dd6a8dc7defcc1
related_topics:
  - title: English version
    url: /en/common/git-checkout.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-checkout.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-checkout.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-checkout.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-checkout.html
    icon: bi bi-globe
---
# git checkout

Extraire une branche ou des chemins vers l'arborescence de travail.
Plus d'informations : <https://git-scm.com/docs/git-checkout>.

- Créer une branche et basculer dessus :

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Créer une branche depuis une référence spécifique et basculer dessus (par exemple, branche locale/distante, tag, commit) :

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">référence</span>

- Basculer sur une branche locale existante :

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Basculer sur la branche précédente :

`git checkout -`

- Basculer sur une branche distante existante :

`git checkout --track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Annule tout les changements dans le répertoire courant (voir `git reset` pour plus de commandes d'annulation) :

`git checkout .`

- Annule tout les changements dans le fichier spécifié :

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Remplace un fichier par sa version d'une autre branche :

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
