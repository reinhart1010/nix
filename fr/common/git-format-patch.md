---
layout: page
title: common/git-format-patch (français)
description: "Préparer des fichiers de correctifs, utiles pour les envoyer par courriel."
content_hash: e077fbf33396eeeebfdd0894592cc32d80917d1e
related_topics:
  - title: English version
    url: /en/common/git-format-patch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-format-patch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-format-patch.html
    icon: bi bi-globe
---
# git format-patch

Préparer des fichiers de correctifs, utiles pour les envoyer par courriel.
Voir également `git am`, qui peut appliquer des fichiers de correctifs générés.
Plus d'informations : <https://git-scm.com/docs/git-format-patch>.

- Créer un fichier de correctif `.patch` nommé automatiquement pour tout les commits non poussés :

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>

- Créer un fichier correctif `.patch` pour les changements entre 2 révisions :

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision_2</span>

- Créer un fichier correctif `.patch` pour les 3 derniers commits :

`git format-patch -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
