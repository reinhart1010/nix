---
layout: page
title: common/docker-service (français)
description: "Gérer les services sur un démon Docker."
content_hash: 58c6b78c05957d16ee100aff9cd842325f5e4b5f
related_topics:
  - title: Deutsch version
    url: /de/common/docker-service.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-service.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-service.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker service

Gérer les services sur un démon Docker.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/service/>.

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
