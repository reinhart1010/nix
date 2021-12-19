---
layout: page
title: common/docker-network (Deutsch)
description: "Erzeuge und verwalte Docker Netzwerke."
content_hash: ddc30f2bc8c0467e89805ba6f9c8d856f959488a
related_topics:
  - title: English version
    url: /en/common/docker-network.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-network.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-network.html
    icon: bi bi-globe
---
# docker network

Erzeuge und verwalte Docker Netzwerke.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/network/>.

- Liste alle verfügbaren und konfigurierten Docker Netzwerke auf:

`docker network ls`

- Erzeuge ein benutzerdefiniertes Netzwerk:

`docker network create --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">treiber_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netzwerk_name</span>

- Zeige detaillierte Informationen der mit Leerzeichen separierten Netzwerke an:

`docker network inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netzwerk_name</span>

- Verbinde einen Container mit einem Netzwerk anhand des Namens oder der ID:

`docker network connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netzwerk_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name|ID</span>

- Trenne einen Container von einem Netzwerk:

`docker network disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netzwerk_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name|ID</span>

- Entferne alle unbenutzten (nicht von Containern referenzierten) Netzwerke:

`docker network prune`

- Entferne mehrere - durch Leerzeichen getrennte - Netzwerke:

`docker network rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netzwerk_name</span>
