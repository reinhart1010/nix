---
layout: page
title: common/docker-service (français)
description: "Gérer les services sur un démon Docker."
content_hash: 5a4538d5d9b77812c1df31bc2944beef9892dba9
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-service.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-service.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-service.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-service.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker service

Gérer les services sur un démon Docker.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/service/>.

- Lister les services sur un démon Docker :

`docker service ls`

- Créer un nouveau service :

`docker service create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_service</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiquette</span>

- Afficher des informations détaillées d'une liste de services séparée par des espaces :

`docker service inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_service|ID</span>

- Lister les tâches d'une liste de services séparée par des espaces :

`docker service ps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_service|ID</span>

- Redimensionner à un nombre spécifique de réplicas pour une liste de services séparée par des espaces :

`docker service scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_service</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count_of_replicas</span>

- Supprimer une liste de services séparée par des espaces :

`docker service rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_service|ID</span>
