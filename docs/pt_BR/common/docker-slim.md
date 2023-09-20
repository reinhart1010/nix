---
layout: page
title: common/docker-slim (português (Brasil))
description: "Analisar e otimizar imagens Docker."
content_hash: 4d45bea6552c22b24f258db981bfcd42d9f9771c
last_modified_at: 2023-09-20
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker-slim

Analisar e otimizar imagens Docker.
Mais informações: <https://github.com/docker-slim/docker-slim>.

- Iniciar o DockerSlim no modo interativo:

`docker-slim`

- Analisar as camadas do Docker a partir de uma imagem específica:

`docker-slim xray --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem:tag</span>

- Verificar um Dockerfile:

`docker-slim lint --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/Dockerfile</span>

- Analisar e gerar uma imagem Docker otimizada:

`docker-slim build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem:tag</span>

- Exibir ajuda para um subcomando:

`docker-slim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` --help`
