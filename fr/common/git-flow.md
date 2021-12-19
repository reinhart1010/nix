---
layout: page
title: common/git-flow (français)
description: "Une collection d'extensions Git pour procurer des opérations supplémentaires sur les dépôts."
content_hash: 48a5b61116356d8b4d389be127d2b0b9fc3563a9
related_topics:
  - title: English version
    url: /en/common/git-flow.html
    icon: bi bi-globe
---
# git flow

Une collection d'extensions Git pour procurer des opérations supplémentaires sur les dépôts.
Plus d'informations : <https://github.com/nvie/gitflow>.

- Initialiser dans un registre Git existant :

`git flow init`

- Commencer le travail sur une fonctionnalité basé sur la branche `develop` :

`git flow feature start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>

- Terminer le travail sur une branche de fonctionnalité, la fusionner dans la branche `develop` puis la supprimer :

`git flow feature finish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>

- Publier une fonctionnalité sur le serveur distant :

`git flow feature publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>

- Récupérer une fonctionnalité publiée par un autre utilisateur :

`git flow feature pull origin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>
