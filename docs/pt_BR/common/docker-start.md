---
layout: page
title: common/docker-start (português (Brasil))
description: "Inicia um ou mais containers parados."
content_hash: e9abb04e8030e4cd5a4c993cd496c5026a63dd7a
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-start.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-start.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-start.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-start.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-start.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker start

Inicia um ou mais containers parados.
Mais informações: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Exibe a ajuda:

`docker start`

- Inicia um container Docker:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Inicia um container, atachando ao terminal os sinais `stdout` e `stderr` e outros sinais:

`docker start --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Inicia um ou mais containers com ID separados por espaço:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>
