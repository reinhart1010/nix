---
layout: page
title: common/docker-container (français)
description: "Gère les conteneurs Docker."
content_hash: b8310fb9c3d4f4ba2563f1bce0da99f58cc4ed9d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-container.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-container.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-container.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-container.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-container.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker container

Gère les conteneurs Docker.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/container/>.

- Liste les conteneurs Dockers en cours d'exécution :

`docker container ls`

- Démarre un ou plusieurs conteneur arrêtés :

`docker container start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_conteneur_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_conteneur_2</span>

- Tue un ou plusieurs conteneurs en cours d'exécution :

`docker container kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_conteneur</span>

- Arrête un ou plusieurs conteneurs en cours d'exécution :

`docker container stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_conteneur</span>

- Mets en pause tous les processus d'un ou plusieurs conteneurs :

`docker container pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_conteneur</span>

- Affiche des informations détaillées sur un ou plusieurs conteneurs :

`docker container inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_conteneur</span>

- Exporte le système de fichiers d'un conteneur sous forme d'archive Tar :

`docker container export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_conteneur</span>

- Crée une nouvelle image à partir des changements d'un conteneur :

`docker container commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_conteneur</span>
