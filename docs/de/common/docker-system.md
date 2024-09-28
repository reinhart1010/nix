---
layout: page
title: common/docker-system (Deutsch)
description: "Verwalte Docker Daten und zeige systemweite Informationen an."
content_hash: ff36d91e2052cc36e79b989ae7c7aef583a560f1
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/common/docker-system.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-system.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-system.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-system.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-system.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker system

Verwalte Docker Daten und zeige systemweite Informationen an.
Weitere Informationen: <https://docs.docker.com/reference/cli/docker/system/>.

- Zeige Hilfe:

`docker system`

- Zeige Docker Festplattennutzung:

`docker system df`

- Zeige detaillierte Informationen zur Festplattennutzung:

`docker system df --verbose`

- Entferne nicht-verwendete Daten:

`docker system prune`

- Entferne nicht-verwendete Daten, die älter als die angegebene Zeit sind:

`docker system prune --filter "until=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stunden</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minuten</span>`m"`

- Zeige Echtzeit-Events vom Docker Daemon:

`docker system events`

- Zeige Echtzeit-Events von Containern und formatiere jede Zeile als gültiges JSON:

`docker system events --filter 'type=container' --format '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .</span>`'`

- Zeige systemweite Informationen:

`docker system info`
