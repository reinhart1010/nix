---
layout: page
title: common/docker-logs (Deutsch)
description: "Zeige Container Logs."
content_hash: afee8497604ad337187992454781b08feb2e7557
last_modified_at: 2024-09-25
related_topics:
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
  - title: português (Brasil) version
    url: /pt_BR/common/docker-logs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-logs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker logs

Zeige Container Logs.
Weitere Informationen: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Zeige die Logs eines Containers:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Zeige die Logs und aktualisiere sie automatisch:

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Zeige die letzten 5 Zeilen:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --tail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Zeige die Logs und füge ihnen Zeitstempel hinzu:

`docker logs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Zeige Logs vor einem bestimmten Zeitpunkt der Ausführung des Containers (bspw. 23m, 10s, 2013-01-02T13:23:37):

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time</span>
