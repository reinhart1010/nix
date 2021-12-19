---
layout: page
title: common/docker-compose (Deutsch)
description: "Starte und verwalte Anwendungen, welche aus mehreren Docker Containern bestehen."
content_hash: 56f713411a73cbaf07a26aa4141497aed57249f3
related_topics:
  - title: English version
    url: /en/common/docker-compose.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker-compose.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
---
# docker-compose

Starte und verwalte Anwendungen, welche aus mehreren Docker Containern bestehen.
Weitere Informationen: <https://docs.docker.com/compose/reference/>.

- Liste alle laufenden Container auf:

`docker-compose ps`

- Erzeuge und starte alle Container im Hintergrund unter der Verwendung der Datei `docker-compose.yml` im aktuellen Verzeichnis:

`docker-compose up -d`

- Starte alle Container. Erzeuge zugehörige Docker Images bei Bedarf neu:

`docker-compose up --build`

- Starte alle Container unter Verwendung einer alternativen Compose Datei:

`docker-compose --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` up`

- Stoppe alle laufenden Container:

`docker-compose stop`

- Stoppe und entferne alle Container inklusive zugehöriger Netzwerke, Volumes und Images:

`docker-compose down --rmi all --volumes`

- Zeige die Logs aller Container kontinuierlich an:

`docker-compose logs --follow`

- Zeige die Logs eines spezifischen Containers kontinuierlich an:

`docker-compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
