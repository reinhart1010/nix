---
layout: page
title: common/docker-machine (français)
description: "Créer et gérer des machines qui exécutent Docker."
content_hash: f281073e4ad1203f5b6968574879696cab121f5a
last_modified_at: 2023-12-20
related_topics:
  - title: Deutsch version
    url: /de/common/docker-machine.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-machine.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-machine.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-machine.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-machine.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-machine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker-machine

Créer et gérer des machines qui exécutent Docker.
Plus d'informations : <https://docs.docker.com/machine/reference/>.

- Lister les machines Docker actuellement en cours d'exécution :

`docker-machine ls`

- Créer une nouvelle machine Docker avec un nom spécifique :

`docker-machine create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Récupérer les informations d'une machine Docker :

`docker-machine status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Démarrer une machine Docker :

`docker-machine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Arrêter une machine Docker :

`docker-machine stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Inspecter les informations d'une machine Docker :

`docker-machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>
