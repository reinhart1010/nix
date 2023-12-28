---
layout: page
title: common/docker-network (português (Brasil))
description: "Criar e gerenciar redes do Docker."
content_hash: a4127a1be36c6c9208e201179800dc01e891c0b1
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-network.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-network.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-network.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-network.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-network.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker network

Criar e gerenciar redes do Docker.
Mais informações: <https://docs.docker.com/engine/reference/commandline/network/>.

- Lista todas as redes disponíveis e configuradas no daemon do Docker:

`docker network ls`

- Cria uma rede definida pelo usuário:

`docker network create --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_driver</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_rede</span>

- Exibe informações detalhadas de uma lista separada por espaços de redes:

`docker network inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_rede</span>

- Conecta um contêiner a uma rede usando um nome ou ID:

`docker network connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_rede</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner|ID</span>

- Desconecta um contêiner de uma rede:

`docker network disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_rede</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner|ID</span>

- Remove todas as redes não utilizadas (que não são referenciadas por nenhum contêiner):

`docker network prune`

- Remove uma lista separada por espaços de redes não utilizadas:

`docker network rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_rede</span>
