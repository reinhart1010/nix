---
layout: page
title: common/docker-rmi (français)
description: "Supprimer une ou plusieurs images Docker."
content_hash: ed351d8a199ef1252460675ad45637b50ca3a8bb
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker rmi

Supprimer une ou plusieurs images Docker.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Afficher l'aide :

`docker rmi`

- Supprimer une ou plusieurs images en fonction de leurs noms :

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1 image2 ...</span>

- Supprimer une image en forçant la suppression :

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Supprimer une image sans supprimer les parents non étiquetés :

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
