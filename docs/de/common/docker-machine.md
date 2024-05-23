---
layout: page
title: common/docker-machine (Deutsch)
description: "Erstelle und verwalte Maschinen, die Docker ausführen."
content_hash: f128fc71ec7c7f3a16694bafe201a3c8f88929bb
last_modified_at: 2024-05-23
related_topics:
  - title: English version
    url: /en/common/docker-machine.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-machine.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-machine.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-machine.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-machine.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-machine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker-machine

Erstelle und verwalte Maschinen, die Docker ausführen.
Weitere Informationen: <https://github.com/docker/machine>.

- Liste zur Zeit laufende Docker Maschinen auf:

`docker-machine ls`

- Erzeuge eine neue Docker Maschine mit einem spezifischen Namen:

`docker-machine create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Zeige den Status einer Maschine:

`docker-machine status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Starte eine Maschine:

`docker-machine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Stoppe eine Maschine:

`docker-machine stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Zeige Informationen über eine Maschine:

`docker-machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
