---
layout: page
title: common/docker-compose (français)
description: "Exécute et gère des applications au travers de plusieurs conteneurs Docker."
content_hash: e094aaff41b5361b5c9a18e000ff94ccebd048a2
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-compose.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-compose.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker-compose.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker compose

Exécute et gère des applications au travers de plusieurs conteneurs Docker.
Plus d'informations : <https://docs.docker.com/compose/reference/>.

- Liste tous les conteneurs en cours d'exécution :

`docker compose ps`

- Crée et démarre en arrière-plan tous les conteneurs décrits dans le fichier `docker-compose.yml` du répertoire courant :

`docker compose up --detach`

- Démarre tous les conteneurs après les avoir recréés si nécessaire :

`docker compose up --build`

- Démarre tous les conteneurs en spécifiant un nom de projet et un fichier compose alternatif :

`docker compose -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_projet</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` up`

- Arrête tous les conteneurs en cours d'exécution :

`docker compose stop`

- Arrête et supprime tous les conteneurs, réseaux, images et volumes :

`docker compose down --rmi all --volumes`

- Affiche et suit la journalisation de tous les conteneurs :

`docker compose logs --follow`

- Affiche et suit la journalisation pour un conteneurs spécifique :

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_container</span>
