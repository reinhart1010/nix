---
layout: page
title: common/docker-machine (português (Brasil))
description: "Criar e gerenciar máquinas que executam o Docker."
content_hash: ff9a06518527c1816620d84c54bab89b50339009
last_modified_at: 2023-09-20
related_topics:
  - title: Deutsch version
    url: /de/common/docker-machine.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-machine.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-machine.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-machine.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-machine.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-machine.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker-machine

Criar e gerenciar máquinas que executam o Docker.
Mais informações: <https://docs.docker.com/machine/reference/>.

- Listar as máquinas Docker em execução no momento:

`docker-machine ls`

- Criar uma nova máquina Docker com um nome específico:

`docker-machine create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Obter o status de uma máquina:

`docker-machine status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Iniciar uma máquina:

`docker-machine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Parar uma máquina:

`docker-machine stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Inspecionar informações sobre uma máquina:

`docker-machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
