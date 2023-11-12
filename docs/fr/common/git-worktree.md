---
layout: page
title: common/git-worktree (français)
description: "Gérer plusieurs arbres de travail attachés au même dépôt."
content_hash: 2c5ec9c128e2ac605bc5012a768d9139a7436bb2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-worktree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-worktree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-worktree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-worktree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git worktree

Gérer plusieurs arbres de travail attachés au même dépôt.
Plus d'informations : <https://git-scm.com/docs/git-worktree>.

- Créer un nouvel arbre de travail avec une branche spécifiée :

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche</span>

- Créer un nouvel arbre de travail avec une nouvelle branche :

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouvelle_branche</span>

- Répertorier tous les arbres de travail attachés à ce dépôt :

`git worktree list`

- Supprimer les arbres de travail (après avoir supprimé les répertoires de travail) :

`git worktree prune`
