---
layout: page
title: common/docker-run (français)
description: "Exécuter une commande dans un nouveau conteneur Docker."
content_hash: 5c201aba4ee395608c46b78b5b5ade46cf4fa6c6
last_modified_at: 2024-09-26
related_topics:
  - title: Deutsch version
    url: /de/common/docker-run.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-run.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-run.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-run.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-run.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker run

Exécuter une commande dans un nouveau conteneur Docker.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/run/>.

- Exécuter une commande dans un nouveau conteneur Docker avec une iamge étiquetée :

`docker run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:etiquette</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Exécuter une commande dans un nouveau contenu Docker en mode détaché (en arrière-plan) et afficher l'ID du conteneur :

`docker run --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Exécuter une command dans un conteneur effemère avec une mode interactif et un terminal pseudo-TTY :

`docker run --rm --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Exécuter une commande dans un nouveau conteneur avec des variables d'environnement :

`docker run --env '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valuer</span>`' --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Exécuter une commande dans un nouveau conteneur avec des volumes montés :

`docker run --volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/l_hote</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/conteneur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Exécuter une commande dans un nouveau conteneur avec des ports publiés :

`docker run --publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_de_l_hote</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_du_conteneur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Exécuter une commande dans un nouveau conteneur en écrasant l'entrée du point d'entrée de l'image :

`docker run --entrypoint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Exécuter une commande dans un nouveau conteneur en le connectant à un réseau :

`docker run --network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reseau</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
