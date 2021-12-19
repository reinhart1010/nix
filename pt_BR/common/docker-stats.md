---
layout: page
title: common/docker-stats (português (Brasil))
description: "Exibe estatísticas dinâmicas de uso de recursos dos containers."
content_hash: 49c197d18027205435a968faffdd9bf220341e95
related_topics:
  - title: Deutsch version
    url: /de/common/docker-stats.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-stats.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-stats.html
    icon: bi bi-globe
---
# docker stats

Exibe estatísticas dinâmicas de uso de recursos dos containers.
Mais informações: <https://docs.docker.com/engine/reference/commandline/stats/>.

- Exibe estatísticas atualizadas de todos os containers em execução:

`docker stats`

- Exibe estatísticas atualizadas de uma lista separada por espaço dos containers:

`docker stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>

- Altera o formato das colunas para exibir o uso da CPU em porcentagem:

`docker stats --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Name</span>`:\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.CPUPerc</span>`"`

- Exibe estatísticas para todos os containers (tanto em execução como parados):

`docker stats --all`

- Desabilita estatísticas atualizadas e só exibe o status naquele momento:

`docker stats --no-stream`
