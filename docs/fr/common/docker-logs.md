---
layout: page
title: common/docker-logs (français)
description: "Affiche les journaux d'un conteneur."
content_hash: 58131884eb22293bbf738b888b9f7cdd2e000ec8
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-logs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-logs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-logs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-logs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-logs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-logs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker logs

Affiche les journaux d'un conteneur.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/logs>.

- Afficher les journaux d'un conteneur :

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>

- Afficher les journaux d'un conteneur en les suivants :

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>

- Afficher les 5 dernière lignes des journaux d'un conteneur :

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>` --tail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Afficher les journaux d'un conteneur avec l'horodatage :

`docker logs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>

- Afficher les journaux d'un conteneur depuis un certain temps (i.e. 23m, 10s, 2013-01-02T13:23:37) :

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>` --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temps</span>
