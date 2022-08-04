---
layout: page
title: common/git-submodule (français)
description: "Inspecter, mettre à jour et manager des sous-modules."
content_hash: fcd4f56a1623889330b8327f145e03d89892dadf
related_topics:
  - title: English version
    url: /en/common/git-submodule.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-submodule.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-submodule.html
    icon: bi bi-globe
---
# git submodule

Inspecter, mettre à jour et manager des sous-modules.
Plus d'informations : <https://git-scm.com/docs/git-submodule>.

- Installer un sous-module depuis le dépôt courant :

`git submodule update --init --recursive`

- Ajout d'un dépôt Git en tant que sous-module :

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>

- Ajout d'un dépôt Git en tant que sous-module à un répertoire donné :

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/repertoire</span>

- Mettre à jour tout les sous-modules à leur dernier commit :

`git submodule foreach git pull`
