---
layout: page
title: common/docker-start (français)
description: "Lancer un ou plusieurs conteneurs arrêtés."
content_hash: 6d98c27fc0cd6773b420c321a0c46f9b0fb5e7ff
related_topics:
  - title: Deutsch version
    url: /de/common/docker-start.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-start.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-start.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-start.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker start

Lancer un ou plusieurs conteneurs arrêtés.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/start/>.

- Afficher l'aide :

`docker start`

- Lancer un conteneur docker :

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>

- Lancer un conteneur, en attachant stdout et stderr et en transférant les signaux :

`docker start --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>

- Lancer un ou plusieurs conteneurs séparés par des espaces :

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur(s)</span>
