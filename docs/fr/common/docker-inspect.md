---
layout: page
title: common/docker-inspect (français)
description: "Retour d'informations de bas niveau sur les objets Docker."
content_hash: 7ab5a2cd91477709b8991610b7c3e5f069c13a94
related_topics:
  - title: Deutsch version
    url: /de/common/docker-inspect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-inspect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-inspect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-inspect.html
    icon: bi bi-globe
---
# docker inspect

Retour d'informations de bas niveau sur les objets Docker.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/inspect/>.

- Montrer l'aide :

`docker inspect`

- Afficher les informations de configuration d'un conteneur, image ou volume en utilisant un nom ou un ID :

`docker inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur|image|ID</span>

- Afficher l'adresse IP d'un conteneur :

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range .NetworkSettings.Networks</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.IPAddress</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>

- Afficher le chemin du fichier journal d'un conteneur :

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.LogPath</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>

- Afficher le nom de l'image d'un conteneur :

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Config.Image</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>

- Afficher les informations de configuration en JSON :

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .Config</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>

- Afficher toutes les liaisons de port :

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range $p, $conf := .NetworkSettings.Ports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$p</span>` -> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(index $conf 0).HostPort</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>
