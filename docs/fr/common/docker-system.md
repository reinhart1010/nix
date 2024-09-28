---
layout: page
title: common/docker-system (français)
description: "Gérer les données Docker et afficher des informations sur l'ensemble du système."
content_hash: 2270c0c89e1fc4b6a9508c79c3901de59853bfe3
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-system.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-system.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-system.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-system.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-system.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker system

Gérer les données Docker et afficher des informations sur l'ensemble du système.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/system/>.

- Afficher l'aide :

`docker system`

- Afficher l'utilisation du disque par Docker :

`docker system df`

- Afficher des informations détaillées sur l'utilisation du disque par Docker :

`docker system df --verbose`

- Supprimer les données non utilisées :

`docker system prune`

- Supprimer les données non utilisées de plus d'un temps donné dans le passé :

`docker system prune --filter "until=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">heures</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutes</span>`m"`

- Afficher les événements du démon Docker en temps réel :

`docker system events`

- Afficher les événements du démon Docker en temps réel avec un format JSON :

`docker system events --filter 'type=container' --format '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .</span>`'`

- Afficher les informations sur le système Docker :

`docker system info`
