---
layout: page
title: linux/login (français)
description: "Démarre une session pour un utilisateur."
content_hash: 8bb197a6047c24b471cb0a3048caef9e4a70d485
related_topics:
  - title: English version
    url: /en/linux/login.html
    icon: bi bi-globe
---
# login

Démarre une session pour un utilisateur.
Plus d'informations : <https://manned.org/login>.

- Démarrer une session en tant qu'utilisateur :

`login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>

- Démarrer une session en tant qu'utilisateur sans authentification si jamais l'utilisateur est déjà pré-authentifié :

`login -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>

- Démarrer une session en tant qu'utilisateur et en préservant l'environnement courant :

`login -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>

- Démarrer une session en tant qu'utilisateur sur un hôte distant :

`login -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>
