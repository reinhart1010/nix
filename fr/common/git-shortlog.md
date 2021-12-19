---
layout: page
title: common/git-shortlog (français)
description: "Récapitule la sortie de `git log`."
content_hash: 3ea5a7c3b3f7b1b4b341e1629cf3a12013229c5d
related_topics:
  - title: English version
    url: /en/common/git-shortlog.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-shortlog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-shortlog.html
    icon: bi bi-globe
---
# git shortlog

Récapitule la sortie de `git log`.
Plus d'informations : <https://git-scm.com/docs/git-shortlog>.

- Afficher un résumé de tous les commits effectués, regroupés par ordre alphabétique par nom d'auteur :

`git shortlog`

- Afficher un résumé de tous les commits effectués, regroupés par le nombre de commits effectués :

`git shortlog -n`

- Afficher un résumé de tous les commits effectués, regroupés par le nom et l'email de l'utilisateur :

`git shortlog -c`

- fficher un résumé des 5 derniers commits effectués :

`git shortlog HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`..HEAD`

- Afficher tout les utilisateurs, emails et le nombre de commits dans la branche :

`git shortlog -sne`

- Afficher tout les utilisateurs, emails et le nombre de commits dans toutes les branches :

`git shortlog -sne --all`
