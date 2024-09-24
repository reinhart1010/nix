---
layout: page
title: common/docker-load (français)
description: "Charge des images Docker depuis des fichiers ou `stdin`."
content_hash: f42a25c02c530a023a264c05a3c46b7cffe0a2a9
last_modified_at: 2024-09-24
related_topics:
  - title: English version
    url: /en/common/docker-load.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-load.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker load

Charge des images Docker depuis des fichiers ou `stdin`.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/load/>.

- Charge une image Docker depuis `stdin` :

`docker load < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_image.tar</span>

- Charge une image Docker depuis un fichier spécifique :

`docker load --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_image.tar</span>

- Charge une image Docker depuis un fichier spécifique en mode silencieux :

`docker load --quiet --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_image.tar</span>
