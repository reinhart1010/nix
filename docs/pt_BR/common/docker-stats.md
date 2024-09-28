---
layout: page
title: common/docker-stats (português (Brasil))
description: "Exibe estatísticas dinâmicas de uso de recursos dos containers."
content_hash: b002f618766f49e3a2e869407b7245265dcdb3a8
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-stats.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-stats.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-stats.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-stats.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker stats

Exibe estatísticas dinâmicas de uso de recursos dos containers.
Mais informações: <https://docs.docker.com/reference/cli/docker/container/stats/>.

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
