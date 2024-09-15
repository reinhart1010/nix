---
layout: page
title: common/docker-rmi (português (Brasil))
description: "Remove uma ou mais imagens Docker."
content_hash: 10d5829b8a330e3402d2dc2ff85daf5c33ace0f3
last_modified_at: 2024-09-15
related_topics:
  - title: Deutsch version
    url: /de/common/docker-rmi.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-rmi.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-rmi.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker rmi

Remove uma ou mais imagens Docker.
Mais informações: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Exibe a ajuda:

`docker rmi`

- Remove uma ou mais imagens pelo seus nomes:

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem1 imagem2 ...</span>

- Remove forçadamente uma imagem:

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Remove uma imagem sem apagar suas imagens pais que não possuem tags:

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>
