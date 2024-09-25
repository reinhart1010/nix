---
layout: page
title: common/docker-logs (italiano)
description: "Mostra i log di un container."
content_hash: 467d1d042a5e8e918a3c7fff6356bb8af3af9fa0
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
  - title: 한국어 version
    url: /ko/common/docker-logs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-logs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-logs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker logs

Mostra i log di un container.
Maggiori informazioni: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Mostra i log di un container:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>

- Segui i log di un container:

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>

- Mostra le ultime 5 righe:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>` --tail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Mostra i log mettendo un timestamp in coda:

`docker logs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>

- Mostra i log avvenuti prima di un dato momento nell'esecuzione del container (ad esempio, 23m, 10s, 2013-01-02T13:23:37):

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>` --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">momento</span>
