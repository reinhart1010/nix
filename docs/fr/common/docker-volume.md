---
layout: page
title: common/docker-volume (français)
description: "Gérer les volumes de Docker."
content_hash: 70c2e29730fa64d5332b705d97614a9db4e93f00
last_modified_at: 2022-12-29
related_topics:
  - title: English version
    url: /en/common/docker-volume.html
    icon: bi bi-globe
---
# docker volume

Gérer les volumes de Docker.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/volume/>.

- Créer un volume :

`docker volume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_volume</span>

- Créer un volume avec une étiquette spécifique :

`docker volume create --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">étiuette</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_volume</span>

- Créer un volume `tmpfs` avec une taille de 100 Mo et un uid de 1000 :

`docker volume create --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>` --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>` --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size=100m,uid=1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_volume</span>

- Lister tous les volumes :

`docker volume ls`

- Supprimer un volume :

`docker volume rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_volume</span>

- Afficher des informations sur un volume :

`docker volume inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_volume</span>

- Supprimer tous les volumes locaux non utilisés :

`docker volume prune`

- Afficher l'aide pour une sous-commande :

`docker volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sous_commande</span>` --help`
