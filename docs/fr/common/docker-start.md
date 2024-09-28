---
layout: page
title: common/docker-start (français)
description: "Lancer un ou plusieurs conteneurs arrêtés."
content_hash: f225d0f6fe8459ffce5110fd853a8217031582bf
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-start.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-start.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-start.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-start.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-start.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker start

Lancer un ou plusieurs conteneurs arrêtés.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/start/>.

- Afficher l'aide :

`docker start`

- Lancer un conteneur Docker :

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>

- Lancer un conteneur, en attachant `stdout` et `stderr` et en transférant les signaux :

`docker start --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>

- Lancer un ou plusieurs conteneurs séparés par des espaces :

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur1 conteneur2 ...</span>
