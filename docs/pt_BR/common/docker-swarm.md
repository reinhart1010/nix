---
layout: page
title: common/docker-swarm (português (Brasil))
description: "Uma ferramenta de orquestração de contêineres."
content_hash: 1bf2fc82c8d289f28590c017fd7327250ce3062f
last_modified_at: 2023-09-20
related_topics:
  - title: Deutsch version
    url: /de/common/docker-swarm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-swarm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-swarm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-swarm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker swarm

Uma ferramenta de orquestração de contêineres.
Mais informações: <https://docs.docker.com/engine/swarm/>.

- Inicializar um cluster do Swarm:

`docker swarm init`

- Exibir o token para ingressar como gerenciador ou trabalhador:

`docker swarm join-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">worker|manager</span>

- Ingressar um novo nó ao cluster:

`docker swarm join --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_do_nó_gerenciador:2377</span>

- Remover um trabalhador do Swarm (executado dentro do nó trabalhador):

`docker swarm leave`

- Exibir o certificado CA atual no formato PEM:

`docker swarm ca`

- Rotacionar o certificado CA atual e exibir o novo certificado:

`docker swarm ca --rotate`

- Alterar o período de validade dos certificados dos nós:

`docker swarm update --cert-expiry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">horas</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutos</span>`m`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>`s`
