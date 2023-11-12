---
layout: page
title: common/git-annex (français)
description: "Gérez les fichiers avec Git, sans archiver leur contenu."
content_hash: 42c52c57fed6548e66aa38bfbeb999fa22de8b27
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-annex.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-annex.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-annex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git annex

Gérez les fichiers avec Git, sans archiver leur contenu.
Lorsqu'un fichier est annexé, son contenu est déplacé dans un stockage clé-valeur et un lien symbolique est créé qui pointe vers le contenu.
Plus d'informations : <https://git-annex.branchable.com>.

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

- Affiche l'aide :

`git annex help`
