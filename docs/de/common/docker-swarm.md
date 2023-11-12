---
layout: page
title: common/docker-swarm (Deutsch)
description: "Ein Container-Orchestrierungswerkzeug."
content_hash: ab07181e27919c2412be4cdba7ab76f51ac70ee9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/docker-swarm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-swarm.html
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

Ein Container-Orchestrierungswerkzeug.
Weitere Informationen: <https://docs.docker.com/engine/swarm/>.

- Initialisiere ein Swarm Cluster:

`docker swarm init`

- Zeige den Token um als Manager oder Worker beizutreten:

`docker swarm join-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">worker|manager</span>

- Füge dem Cluster eine neue Node hinzu:

`docker swarm join --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">manager_node_url:2377</span>

- Entferne einen Worker vom Swarm (führe dies auf der Worker Node aus):

`docker swarm leave`

- Zeige die aktuellen CA Zertifikate im PEM Format:

`docker swarm ca`

- Rotiere die aktuellen CA Zertifikate und zeige die neuen Zertifikate:

`docker swarm ca --rotate`

- Ändere die Gültigkeitsdauer für Node-Zertifikate:

`docker swarm update --cert-expiry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stunden</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minuten</span>`m`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sekunden</span>`s`
