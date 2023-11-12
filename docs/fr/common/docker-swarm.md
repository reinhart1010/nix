---
layout: page
title: common/docker-swarm (français)
description: "Outil d'orchestration de conteneurs."
content_hash: 9d7cffbf79defbc2222d8b7665935522a72aee78
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-swarm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-swarm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-swarm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-swarm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker swarm

Outil d'orchestration de conteneurs.
Plus d'informations : <https://docs.docker.com/engine/swarm/>.

- Initialiser un cluster swarm :

`docker swarm init`

- Afficher le jeton pour rejoindre un cluster swarm en tant que nœud manager ou worker :

`docker swarm join-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">worker|manager</span>

- Rejoindre un nouveau nœud au cluster :

`docker swarm join --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jeton</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_du_manager:2377</span>

- Supprimer un worker du cluster (à exécuter dans le nœud worker) :

`docker swarm leave`

- Afficher le certificat CA actuel au format PEM :

`docker swarm ca`

- Changer la certificat CA actuel et afficher le nouveau certificat :

`docker swarm ca --rotate`

- Changer la période de validité des certificats des nœuds :

`docker swarm update --cert-expiry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">heures</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutes</span>`m`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secondes</span>`s`
