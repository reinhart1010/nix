---
layout: page
title: common/docker-compose (português (Brasil))
description: "Executa e gerencia multi-containers de aplicações Docker."
content_hash: d56b0f12d199e2db7280b0ef9dd70c4061724b1f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-compose.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-compose.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker-compose.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-compose.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker compose

Executa e gerencia multi-containers de aplicações Docker.
Mais informações: <https://docs.docker.com/compose/reference/>.

- Lista todos os containers em execução:

`docker compose ps`

- Cria e inicia todos os containers em segundo plano usando um arquivo `docker-compose.yml` do seu diretório atual:

`docker compose up --detach`

- Inicia todos os containers. Se necessário, realiza um rebuild:

`docker compose up --build`

- Inicia todos os containers que estão usando um arquivo compose alternativo:

`docker compose --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` up`

- Encerra todos os containers em execução:

`docker compose stop`

- Encerra e remove todos os containers, networks, imagens e volumes:

`docker compose down --rmi all --volumes`

- Segue os logs de todos os containers:

`docker compose logs --follow`

- Segue os logs de um container específico:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>
