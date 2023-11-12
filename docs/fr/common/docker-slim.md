---
layout: page
title: common/docker-slim (français)
description: "Analyser et optimiser les images Docker."
content_hash: 1f728d0ecec8075b0aa66a0746683fac8a65cea0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-slim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-slim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-slim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker-slim

Analyser et optimiser les images Docker.
Plus d'informations : <https://github.com/docker-slim/docker-slim>.

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
