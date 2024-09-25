---
layout: page
title: common/docker-network (français)
description: "Créer et gérer des réseaux Docker."
content_hash: ae1ed3b1950f1f914f8943c6e4786c1c4f358436
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/common/docker-network.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-network.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-network.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-network.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-network.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker network

Créer et gérer des réseaux Docker.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/network/>.

- Lister tous les réseaux disponible et configuré du service Docker :

`docker network ls`

- Créer un réseau défini par l'utilisateur :

`docker network create --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_driver</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_reseau</span>

- Afficher les informations détaillées des réseaux séparés par des espaces :

`docker network inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_reseau</span>

- Connecter un conteneur à un réseau en utilisant un nom  ou  un ID :

`docker network connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_reseau</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur|ID</span>

- Déconnecter un conteneur d'un réseau en utilisant un nom ou un ID :

`docker network disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_reseau</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur|ID</span>

- Supprimer tous les réseaux non utilisés (non reliés à un conteneur) :

`docker network prune`

- Supprimer les réseaux séparés par des espaces :

`docker network rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_reseau</span>
