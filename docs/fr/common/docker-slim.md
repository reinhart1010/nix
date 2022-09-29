---
layout: page
title: common/docker-slim (français)
description: "Analyser et optimiser les images Docker."
content_hash: 2c1b4edbd1a65b24c3b78a98453711b0eaaf799d
related_topics:
  - title: Deutsch version
    url: /de/common/docker-slim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-slim.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker-slim

Analyser et optimiser les images Docker.
Plus d'informatiosn : <https://github.com/docker-slim/docker-slim>.

- Démarrer DockerSlim en mode interactif :

`docker-slim`

- Analyser les couches Docker à partir d'une image spécifique :

`docker-slim xray --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:etiquette</span>

- Linter un Dockerfile :

`docker-slim lint --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/Dockerfile</span>

- Analyser et générer une image Docker optimisée :

`docker-slim build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:etiquette</span>

- Afficher l'aide pour une sous-commande :

`docker-slim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommande</span>` --help`
