---
layout: page
title: common/docker-network (Deutsch)
description: "Erzeuge und verwalte Docker Netzwerke."
content_hash: 991c2d3b8dec02687dd584be6eac0a99791261ae
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/docker-network.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-network.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-network.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-network.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-network.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker network

Erzeuge und verwalte Docker Netzwerke.
Weitere Informationen: <https://docs.docker.com/reference/cli/docker/network/>.

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
