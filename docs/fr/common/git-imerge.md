---
layout: page
title: common/git-imerge (français)
description: "Générer un `git merge` ou un `git rebase` entre deux branches de manière incrémentale."
content_hash: d8857e2401e304b7d94f17e6661ecd34c6a30438
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-imerge.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-imerge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-imerge.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-imerge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git-imerge

Générer un `git merge` ou un `git rebase` entre deux branches de manière incrémentale.
Les conflits entre les branches sont suivis en paires de commits individuels, pour simplifier la résolution des conflits.
Plus d'informations : <https://github.com/mhagger/git-imerge>.

- Démarrer un imerge rebase (se placer dans la branche à rebaser d'abord) :

`git imerge rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche_sur_laquelle_rebaser</span>

- Démarrer imerge merge (se placer dans la branche depuis laquelle merger d'abord) :

`git imerge merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche_a_merger</span>

- Afficher le diagramme ASCII du merge ou rebase en cours :

`git imerge diagram`

- Continuer l'opération après une résolution de conflit (d'abord `git add` les fichiers en conflits) :

`git imerge continue --no-edit`

- Terminer l'opération i-merge après la résolution de tous les conflits :

`git imerge finish`

- Annuler l'opération et retourner à la branche précédente :

`git-imerge remove && git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">previous_branch</span>
