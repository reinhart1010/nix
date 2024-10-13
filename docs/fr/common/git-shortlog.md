---
layout: page
title: common/git-shortlog (français)
description: "Récapitule la sortie de `git log`."
content_hash: 9802650e67cdc670aaf4a662b5448efc2a6dea90
last_modified_at: 2024-10-13
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
  - title: 한국어 version
    url: /ko/common/git-shortlog.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-shortlog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git shortlog

Récapitule la sortie de `git log`.
Plus d'informations : <https://git-scm.com/docs/git-shortlog>.

- Afficher un résumé de tous les commits effectués, regroupés par ordre alphabétique par nom d'auteur :

`git shortlog`

- Afficher un résumé de tous les commits effectués, regroupés par le nombre de commits effectués :

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>

- Afficher un résumé de tous les commits effectués, regroupés par le nom et l'email de l'utilisateur :

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--committer</span>

- Afficher un résumé des 5 derniers commits effectués :

`git shortlog HEAD~5..HEAD`

- Afficher tout les utilisateurs, emails et le nombre de commits dans la branche :

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--summary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--email</span>

- Afficher tout les utilisateurs, emails et le nombre de commits dans toutes les branches :

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--summary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--email</span>` --all`
