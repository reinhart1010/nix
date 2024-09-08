---
layout: page
title: common/docker-ps (português (Brasil))
description: "Lista os containers Docker."
content_hash: 175bc7078ad6086acba54c267e229858fc68b9b2
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/docker-ps.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-ps.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-ps.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker ps

Lista os containers Docker.
Mais informações: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Lista containers Docker em execução:

`docker ps`

- Lista todos containers Docker (em execução e parados):

`docker ps --all`

- Lista os últimos containers criados (incluí todos os estados):

`docker ps --latest`

- Filtra os containers que contém uma substring no seu nome:

`docker ps --filter="name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`"`

- Filtra todos os containers que possuem uma imagem antepassada:

`docker ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`"`

- Filtra containers que tenha o código de saída:

`docker ps --all --filter="exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">código</span>`"`

- Filtra containers por estado (criado, execução, removendo, pausado, finalizado e morto):

`docker ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">estado</span>`"`

- Filtra containers que contenham um volume específico ou montado em um caminho específico:

`docker ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
