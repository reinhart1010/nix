---
layout: page
title: common/docker-machine (português (Brasil))
description: "Criar e gerenciar máquinas que executam o Docker."
content_hash: b63cf95f2c63a24a3a8dbb55376d3537727c6c8f
last_modified_at: 2024-05-23
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
tldri18n_status: 2
---
# docker-machine

Criar e gerenciar máquinas que executam o Docker.
Mais informações: <https://github.com/docker/machine>.

- Lista as máquinas Docker em execução no momento:

`docker-machine ls`

- Cria uma nova máquina Docker com um nome específico:

`docker-machine create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Obtém o status de uma máquina:

`docker-machine status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Inicia uma máquina:

`docker-machine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Para uma máquina:

`docker-machine stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Inspeciona informações sobre uma máquina:

`docker-machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
