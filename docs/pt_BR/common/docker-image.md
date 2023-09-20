---
layout: page
title: common/docker-image (português (Brasil))
description: "Gerenciar imagens do Docker."
content_hash: ef9901eae9d83e9ed3709b997e15f7fce294618a
last_modified_at: 2023-09-20
related_topics:
  - title: Deutsch version
    url: /de/common/docker-image.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-image.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-image.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-image.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-image.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker image

Gerenciar imagens do Docker.
Veja também `docker build`, `docker import` e `docker pull`.
Mais informações: <https://docs.docker.com/engine/reference/commandline/image/>.

- Listar imagens Docker locais:

`docker image ls`

- Excluir imagens Docker locais não utilizadas:

`docker image prune`

- Excluir todas as imagens não utilizadas (não apenas aquelas sem uma tag):

`docker image prune --all`

- Mostrar o histórico de uma imagem Docker local:

`docker image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>
