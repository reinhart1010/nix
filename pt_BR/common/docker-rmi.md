---
layout: page
title: common/docker-rmi (português (Brasil))
description: "Remove uma ou mais imagens Docker."
content_hash: 26f0fb4901eb505f62a48ae3f5562551b67cedcd
related_topics:
  - title: Deutsch version
    url: /de/common/docker-rmi.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-rmi.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-rmi.html
    icon: bi bi-globe
---
# docker rmi

Remove uma ou mais imagens Docker.
Mais informações: <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Exibe a ajuda:

`docker rmi`

- Remove uma ou mais imagens pelo seus nomes:

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem1 imagem2 ...</span>

- Remove forçadamente uma imagem:

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Remove uma imagem sem apagar suas imagens pais que não possuem tags:

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>
