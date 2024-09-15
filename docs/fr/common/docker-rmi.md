---
layout: page
title: common/docker-rmi (français)
description: "Supprimer une ou plusieurs images Docker."
content_hash: bdf4a5ac2965bec97d642dd0238580bdb43aa1ca
last_modified_at: 2024-09-15
related_topics:
  - title: Deutsch version
    url: /de/common/docker-rmi.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-rmi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-rmi.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker rmi

Supprimer une ou plusieurs images Docker.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Afficher l'aide :

`docker rmi`

- Supprimer une ou plusieurs images en fonction de leurs noms :

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1 image2 ...</span>

- Supprimer une image en forçant la suppression :

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Supprimer une image sans supprimer les parents non étiquetés :

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
