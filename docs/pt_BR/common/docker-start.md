---
layout: page
title: common/docker-start (português (Brasil))
description: "Inicia um ou mais containers parados."
content_hash: 8c68ac08ec050c2684b937b4de21f219914c946f
last_modified_at: 2024-03-14
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
Mais informações: <https://docs.docker.com/engine/reference/commandline/start/>.

- Exibe a ajuda:

`docker start`

- Inicia um container Docker:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Inicia um container, atachando ao terminal os sinais `stdout` e `stderr` e outros sinais:

`docker start --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Inicia um ou mais containers com ID separados por espaço:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>
