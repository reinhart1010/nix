---
layout: page
title: common/git-annex (français)
description: "Gérez les fichiers avec Git, sans archiver leur contenu."
content_hash: 7f10b0eb75e91596558176090e716765bad939e6
related_topics:
  - title: English version
    url: /en/common/git-annex.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-annex.html
    icon: bi bi-globe
---
# git annex

Gérez les fichiers avec Git, sans archiver leur contenu.
Lorsqu'un fichier est annexé, son contenu est déplacé dans un stockage clé-valeur et un lien symbolique est créé qui pointe vers le contenu.
Plus d'informations : <https://git-annex.branchable.com>.

- Aide :

`git annex help`

- Initialise le dépôt :

`git annex init`

- Ajoute un fichier :

`git annex add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_repertoire</span>

- Affiche le statut courant d'un fichier ou répertoire :

`git annex status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_repertoire</span>

- Synchronise un dépôt local avec un distant :

`git annex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distant</span>

- Récupère un fichier ou un répertoire :

`git annex get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_repertoire</span>
