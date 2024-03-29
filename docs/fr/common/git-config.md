---
layout: page
title: common/git-config (français)
description: "Gérer les options de configuration personnalisées pour les référentiels Git."
content_hash: 6731e547c9d80cfc2bdb179e1eeeb2dacfc0a475
last_modified_at: 2024-01-16
related_topics:
  - title: Deutsch version
    url: /de/common/git-config.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-config.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-config.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git config

Gérer les options de configuration personnalisées pour les référentiels Git.
Ces configurations peuvent être locales (pour le référentiel courant) ou globales (pour l'utilisateur).
Plus d'informations : <https://git-scm.com/docs/git-config>.

- Liste les entrées de configurations locales (stockées dans `.git/config` du répertoire courant) :

`git config --list --local`

- Liste les entrées de configuration globales (stockées dans `~/.gitconfig`) :

`git config --list --global`

- Récupère la valeur d'une entrée de configuration :

`git config alias.unstage`

- Attribue la valeur d'une entrée de configuration :

`git config --global alias.unstage "reset HEAD --"`

- Restaure la valeur d'une entrée de configuration globale à sa valeur par défaut :

`git config --global --unset alias.unstage`

- Édite le fichier de configuration du référentiel courant dans l'éditeur par défaut :

`git config --edit`

- Édite le fichier de configuration globale dans l'éditeur par défaut :

`git config --global --edit`
