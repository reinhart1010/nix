---
layout: page
title: common/docker-pull (français)
description: "Télécharge une image Docker depuis le registre."
content_hash: 5b2885af443a04cfd2af0665c381327cc079fc5a
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/docker-pull.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker pull

Télécharge une image Docker depuis le registre.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/pull/>.

- Télécharge une image Docker spécifique :

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">étiquette</span>

- Télécharge une image Docker spécifique en mode silencieux :

`docker pull --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">étiquette</span>

- Télécharge toutes les étiquettes d'une image Docker spécifique :

`docker pull --all-tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Télécharge un image Docker pour une plateforme spécifique, ex : linux/amd64 :

`docker pull --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux/amd64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">étiquette</span>

- Affiche l'aide :

`docker pull --help`
