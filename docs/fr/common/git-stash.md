---
layout: page
title: common/git-stash (français)
description: "Stocker les modifications Git locales dans une zone temporaire."
content_hash: b43fe7c19fdafa52c10851e729aee99c5dff9b0f
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/git-stash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-stash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-stash.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-stash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git stash

Stocker les modifications Git locales dans une zone temporaire.
Plus d'informations : <https://git-scm.com/docs/git-stash>.

- Stocker les changements courants, sauf les fichiers non-suivis :

`git stash push -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_stash_optionel</span>

- Stocker les changements courants, incluant les fichiers non-suivis :

`git stash -u`

- Stocker les parties d'un fichier interactivement :

`git stash -p`

- Lister tous les stashs (affiche leurs noms, les branches relatives et messages) :

`git stash list`

- Applique un stash (par défaut, le dernier, nommé stash@{0}) :

`git stash apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_stash_ou_de_commit_optionel</span>

- Applique un stash (par défaut le dernier, stash@{0}), et le supprimer de la liste des stashs s'il n'y a pas de conflit :

`git stash pop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_stash_optionel</span>

- Supprime tous les stashs :

`git stash clear`
