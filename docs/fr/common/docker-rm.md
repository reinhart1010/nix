---
layout: page
title: common/docker-rm (français)
description: "Supprime un ou plusieurs conteneurs."
content_hash: 4f99ad9c7448140f447cf910aff84fdec5ac7851
last_modified_at: 2024-09-17
related_topics:
  - title: English version
    url: /en/common/docker-rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/docker-rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker rm

Supprime un ou plusieurs conteneurs.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/rm/>.

- Supprimer des conteneurs :

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur1 conteneur2 ...</span>

- Supprimer des conteneurs par la force :

`docker rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur1 conteneur2 ...</span>

- Supprimer un conteneur et ses volumes :

`docker rm --volumes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>

- Affiche l'aide :

`docker rm --help`
