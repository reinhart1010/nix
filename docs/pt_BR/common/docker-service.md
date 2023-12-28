---
layout: page
title: common/docker-service (português (Brasil))
description: "Gerenciar os serviços em um daemon do Docker."
content_hash: 51b6c944164a37ace257e59064c2cd8458276866
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-service.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-service.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-service.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-service.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker service

Gerenciar os serviços em um daemon do Docker.
Mais informações: <https://docs.docker.com/engine/reference/commandline/service/>.

- Lista os serviços em um daemon do Docker:

`docker service ls`

- Cria um novo serviço:

`docker service create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Exibe informações detalhadas de uma lista separada por espaços de serviços:

`docker service inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço|ID</span>

- Lista as tarefas de uma lista separada por espaços de serviços:

`docker service ps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço|ID</span>

- Escala para um número específico de réplicas para uma lista separada por espaços de serviços:

`docker service scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quantidade_de_réplicas</span>

- Remove uma lista separada por espaços de serviços:

`docker service rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço|ID</span>
