---
layout: page
title: common/docker-logs (português (Brasil))
description: "Exibe os logs dos containers."
content_hash: dcd161bf378ff4b97a5102585d8a473d2152dce1
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/common/docker-logs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-logs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-logs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-logs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-logs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-logs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker logs

Exibe os logs dos containers.
Mais informações: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Exibe logs de um container:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>

- Exibe logs de um container e segue exibindo:

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>

- Exibe as últimas 5 linhas:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>` --tail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Exibe logs e adiciona a informação de hora ao log:

`docker logs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>

- Exibe logs até um certo ponto no tempo de execução do container (por exemplo: 23m, 10s, 2013-01-02T13:23:37):

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>` --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tempo</span>
