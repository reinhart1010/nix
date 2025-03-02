---
layout: page
title: common/docker-image (français)
description: "Gérer les images Docker."
content_hash: 3790c0d5be55ca733c6cf997a4f1cdf9d69a5f41
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/docker-image.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-image.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-image.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-image.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-image.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker image

Gérer les images Docker.
Voir aussi `docker build`, `docker import`, and `docker pull`.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/>.

- Lister les images Docker locales :

`docker image ls`

- Supprimer les images Docker locales inutilisées :

`docker image prune`

- Supprimer toutes les images inutilisées (pas seulement celles sans étiquette) :

`docker image prune --all`

- Afficher l'historique d'une image Docker locale :

`docker image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
