---
layout: page
title: common/docker-service (Deutsch)
description: "Verwalte Docker Services."
content_hash: 5ee8df70ce9a54c145437edb747118df7c0c7ff1
related_topics:
  - title: English version
    url: /en/common/docker-service.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-service.html
    icon: bi bi-globe
---
# docker service

Verwalte Docker Services.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/service/>.

- Liste alle Services auf:

`docker service ls`

- Erstelle einen neuen Service:

`docker service create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Zeige detaillierte Informationen der mit Leerzeichen separierten Services an:

`docker service inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name|ID</span>

- Liste die Tasks der mit Leerzeichen separierten Services auf:

`docker service ps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name|ID</span>

- Skaliere die angegebenen Services auf einen bestimmte Anzahl an Replikaten:

`docker service scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_replikaten</span>

- Lösche die mit Leerzeichen separierten Services:

`docker service rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name|ID</span>
