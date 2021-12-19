---
layout: page
title: common/git-stage (français)
description: "Ajouter le contenu du fichier à la zone de préparation."
content_hash: 506238e039a4f48b93a823f99ff969ee5902f768
related_topics:
  - title: English version
    url: /en/common/git-stage.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-stage.html
    icon: bi bi-globe
---
# git stage

Ajouter le contenu du fichier à la zone de préparation.
Synonyme de `git add`.
Plus d'informations : <https://git-scm.com/docs/git-stage>.

- Ajouter un fichier à l'index :

`git stage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Ajoute tous les fichiers à l'index (suivis et non-suivis) :

`git stage -A`

- Ajout uniquement des fichiers déjà suivis :

`git stage -u`

- Ajout également des fichiers ignorés :

`git stage -f`

- Ajout des fichiers par parties, interactivement :

`git stage -p`

- Ajout d'un fichier par parties, interactivement :

`git stage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Ajout d'un fichier, interactivement :

`git stage -i`
