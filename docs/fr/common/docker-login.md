---
layout: page
title: common/docker-login (français)
description: "Se connecter à un registre Docker."
content_hash: 664fde5d93f11aa7691c0dd8f9af0fe2983ba70b
related_topics:
  - title: Deutsch version
    url: /de/common/docker-login.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-login.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker login

Se connecter à un registre Docker.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/login/>.

- Se connecter de manière interactive à un registre :

`docker login`

- Se connecter à un registre avec un nom d'utilisateur spécifique (l'utilisateur sera invité à saisir un mot de passe) :

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>

- Se connecter à un registre avec un nom d'utilisateur et un mot de passe spécifiques :

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serveur</span>

- Se connecter à un registre avec un mot de passe depuis l'entrée standard :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>`" | docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>` --password-stdin`
