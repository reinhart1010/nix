---
layout: page
title: common/docker-ps (français)
description: "Lister les conteneurs Docker."
content_hash: 2b41497655f25fa1528405d0b545e6d1526e6daf
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/docker-ps.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-ps.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-ps.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker ps

Lister les conteneurs Docker.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Lister les conteneurs Docker en cours d'exécution :

`docker ps`

- Lister tous les conteneurs Docker (en cours d'exécution et arrêtés) :

`docker ps --all`

- Afficher le dernier conteneur Docker créé (avec tous les états) :

`docker ps --latest`

- Afficher les conteneurs avec une chaine de caractère dans leur nom :

`docker ps --filter "name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`

- Afficher les conteneurs avec une même image comme parent :

`docker ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiquette</span>`"`

- Afficher les conteneurs avec un code de sorti spécifique :

`docker ps --all --filter="exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Afficher les conteneurs avec un statut spécifique (créé, en cours d'exécution, en cours de suppresion, en pause, arrêté, mort) :

`docker ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>`"`

- Afficher les conteneurs avec un point de montage spécifique :

`docker ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/dossier</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
