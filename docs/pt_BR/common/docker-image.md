---
layout: page
title: common/docker-image (português (Brasil))
description: "Gerencia imagens do Docker."
content_hash: f5b82cd045942c744ea9cf3df2185e9052c2d28c
last_modified_at: 2024-09-23
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
tldri18n_status: 2
---
# docker image

Gerencia imagens do Docker.
Veja também `docker build`, `docker import` e `docker pull`.
Mais informações: <https://docs.docker.com/reference/cli/docker/image/>.

- Lista imagens Docker locais:

`docker image ls`

- Exclui imagens Docker locais não utilizadas:

`docker image prune`

- Exclui todas as imagens não utilizadas (não apenas aquelas sem uma etiqueta):

`docker image prune --all`

- Mostra o histórico de uma imagem Docker local:

`docker image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>
