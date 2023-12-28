---
layout: page
title: common/docker-slim (português (Brasil))
description: "Analisar e otimizar imagens Docker."
content_hash: 113288392bec0d97d955659ebc2f7681f61491d1
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-slim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-slim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-slim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker-slim

Analisar e otimizar imagens Docker.
Mais informações: <https://github.com/docker-slim/docker-slim>.

- Inicia o DockerSlim no modo interativo:

`docker-slim`

- Analisa as camadas do Docker a partir de uma imagem específica:

`docker-slim xray --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem:tag</span>

- Verifica um Dockerfile:

`docker-slim lint --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/Dockerfile</span>

- Analisa e gera uma imagem Docker otimizada:

`docker-slim build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem:tag</span>

- Exibe ajuda para um subcomando:

`docker-slim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` --help`
