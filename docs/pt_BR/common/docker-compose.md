---
layout: page
title: common/docker-compose (português (Brasil))
description: "Executa e gerencia multi-containers de aplicações Docker."
content_hash: ae25ad230ac215dd09e333e533fd2234ceda1cf0
last_modified_at: 2024-09-14
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
Mais informações: <https://docs.docker.com/reference/cli/docker/compose/>.

- Lista todos os containers em execução:

`docker compose ps`

- Cria e inicia todos os containers em segundo plano usando um arquivo `docker-compose.yml` do seu diretório atual:

`docker compose up --detach`

- Inicia todos os containers. Se necessário, realiza um rebuild:

`docker compose up --build`

- Inicia todos os containers especificando um nome de projeta e usando um arquivo de composição alternativo:

`docker compose -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_projeto</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` up`

- Encerra todos os containers em execução:

`docker compose stop`

- Encerra e remove todos os containers, networks, imagens e volumes:

`docker compose down --rmi all --volumes`

- Segue os logs de todos os containers:

`docker compose logs --follow`

- Segue os logs de um container específico:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>
