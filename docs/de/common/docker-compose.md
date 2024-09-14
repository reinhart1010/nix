---
layout: page
title: common/docker-compose (Deutsch)
description: "Starte und verwalte Anwendungen, welche aus mehreren Docker Containern bestehen."
content_hash: 00458a1b5c3ca8fb44e18758cf2271f166b8dc4a
last_modified_at: 2024-09-14
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
  - title: Indonesia version
    url: /id/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker compose

Starte und verwalte Anwendungen, welche aus mehreren Docker Containern bestehen.
Weitere Informationen: <https://docs.docker.com/reference/cli/docker/compose/>.

- Liste alle laufenden Container auf:

`docker compose ps`

- Erzeuge und starte alle Container im Hintergrund unter der Verwendung der Datei `docker-compose.yml` im aktuellen Verzeichnis:

`docker compose up --detach`

- Starte alle Container. Erzeuge zugehörige Docker Images bei Bedarf neu:

`docker compose up --build`

- Starte alle Container durch Angabe eines Projektnamens unter Verwendung einer alternativen Compose-Datei:

`docker compose -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Projektname</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` up`

- Stoppe alle laufenden Container:

`docker compose stop`

- Stoppe und entferne alle Container inklusive zugehöriger Netzwerke, Volumes und Images:

`docker compose down --rmi all --volumes`

- Zeige die Logs aller Container kontinuierlich an:

`docker compose logs --follow`

- Zeige die Logs eines spezifischen Containers kontinuierlich an:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
