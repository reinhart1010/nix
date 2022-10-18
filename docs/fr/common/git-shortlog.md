---
layout: page
title: common/git-shortlog (français)
description: "Récapitule la sortie de `git log`."
content_hash: d2ee4705350d6281b9b30d0f4a026143bba4ba5c
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
  - title: Türkçe version
    url: /tr/common/git-shortlog.html
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

- Afficher un résumé des 5 derniers commits effectués :

`git shortlog HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`..HEAD`

- Afficher tout les utilisateurs, emails et le nombre de commits dans la branche :

`git shortlog -sne`

- Afficher tout les utilisateurs, emails et le nombre de commits dans toutes les branches :

`git shortlog -sne --all`
