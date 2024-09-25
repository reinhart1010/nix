---
layout: page
title: common/docker-login (français)
description: "Se connecter à un registre Docker."
content_hash: 43292b021d6d7ed909bc01f76e71626eeadeb300
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/common/docker-login.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-login.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker login

Se connecter à un registre Docker.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/login/>.

- Se connecter de manière interactive à un registre :

`docker login`

- Se connecter à un registre avec un nom d'utilisateur spécifique (l'utilisateur sera invité à saisir un mot de passe) :

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>

- Se connecter à un registre avec un nom d'utilisateur et un mot de passe spécifiques :

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serveur</span>

- Se connecter à un registre avec un mot de passe depuis l'entrée standard :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>`" | docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>` --password-stdin`
