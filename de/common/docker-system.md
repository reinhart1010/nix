---
layout: page
title: common/docker-system (Deutsch)
description: "Verwalte Docker Daten und zeige systemweite Informationen an."
content_hash: d8b2d4cb2d85a4b85c1a1f3320cacb4174b83649
related_topics:
  - title: English version
    url: /en/common/docker-system.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-system.html
    icon: bi bi-globe
---
# docker system

Verwalte Docker Daten und zeige systemweite Informationen an.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/system/>.

- Zeige Hilfe:

`docker system`

- Zeige Docker Festplattennutzung:

`docker system df`

- Zeige detaillierte Informationen zur Festplattennutzung:

`docker system df --verbose`

- Entferne nicht-verwendete Daten:

`docker system prune`

- Entferne nicht-verwendete Daten, die älter als die angegeben Zeit sind:

`docker system prune --filter="until=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stunden</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minuten</span>`m"`

- Zeige Echtzeit-Events vom Docker Daemon:

`docker system events`

- Zeige Echtzeit-Events von Containern und formatiere jede Zeile als gültiges JSON:

`docker system events --filter 'type=container' --format '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .</span>`'`

- Zeige systemweite Informationen:

`docker system info`
