---
layout: page
title: common/git-log (français)
description: "Afficher un historique de commits."
content_hash: 6921bd489ac268bde672ff12ba1e3a2c25f1a63b
related_topics:
  - title: Deutsch version
    url: /de/common/git-log.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-log.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-log.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-log.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-log.html
    icon: bi bi-globe
---
# git log

Afficher un historique de commits.
Plus d'informations : <https://git-scm.com/docs/git-log>.

- Afficher la séquence de commits à partir de l'actuel, dans l'ordre chronologique inverse du dépôt Git dans le répertoire de travail actuel :

`git log`

- Afficher l'historique de fichiers ou répertoires en particulier :

`git log -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_repertoire</span>

- Afficher la liste des fichiers modifiés pour chaque commit :

`git log --stat`

- Afficher un graphique des commits dans la branche actuelle en utilisant uniquement la première ligne de chaque message de commit :

`git log --oneline --graph`

- Afficher un graphique de tout les commits, tags et branches dans le dépôt entier :

`git log --oneline --decorate --all --graph`

- Afficher uniquement les commits dont le message contient la chaine (non sensible à la casse) :

`git log -i --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaine_recherché</span>

- Afficher les N derniers commits d'un utilisateur :

`git log -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` --author=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author</span>

- Afficher les commits entre deux dates (yyyy-mm-dd):

`git log --before="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-29</span>`" --after="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-17</span>`"`
