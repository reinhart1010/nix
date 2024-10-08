---
layout: page
title: common/docker (Nederlands)
description: "Beheer Docker containers en images."
content_hash: cfe7988ea5d4af2b84128bbb206b0d8df9d66e3c
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/common/docker.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/docker.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker

Beheer Docker containers en images.
Sommige subcommando's zoals `run` hebben hun eigen documentatie.
Meer informatie: <https://docs.docker.com/reference/cli/docker/>.

- Toon alle Docker containers (actief en gestopte):

`docker ps --all`

- Start een container van een image, met een aangepaste naam:

`docker run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Start of stop een bestaande container:

`docker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_naam</span>

- Download een image uit een Docker register:

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Toon reeds gedownloade images:

`docker images`

- Open een shell in een actieve container:

`docker exec -it `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- Verwijder een gestopte container:

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_naam</span>

- Volg de logs van een container:

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_naam</span>
