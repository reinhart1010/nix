---
layout: page
title: common/docker-swarm (português (Brasil))
description: "Uma ferramenta de orquestração de contêineres."
content_hash: ab570320f71ecab61fbeaf2f69e175d82e398770
last_modified_at: 2023-12-28
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
tldri18n_status: 2
---
# docker swarm

Uma ferramenta de orquestração de contêineres.
Mais informações: <https://docs.docker.com/engine/swarm/>.

- Inicializa um cluster do Swarm:

`docker swarm init`

- Exibe o token para ingressar como gerenciador ou trabalhador:

`docker swarm join-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">worker|manager</span>

- Ingressa um novo nó ao cluster:

`docker swarm join --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_do_nó_gerenciador:2377</span>

- Remove um trabalhador do Swarm (executado dentro do nó trabalhador):

`docker swarm leave`

- Exibe o certificado CA atual no formato PEM:

`docker swarm ca`

- Rotaciona o certificado CA atual e exibe o novo certificado:

`docker swarm ca --rotate`

- Altera o período de validade dos certificados dos nós:

`docker swarm update --cert-expiry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">horas</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutos</span>`m`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>`s`
