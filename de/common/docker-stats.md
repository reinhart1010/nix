---
layout: page
title: common/docker-stats (Deutsch)
description: "Zeige den Ressourcen-Verbrauch von Containern in Echtzeit."
content_hash: d1abb60f62c98a221848e26220e60a3079a8487f
related_topics:
  - title: English version
    url: /en/common/docker-stats.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-stats.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-stats.html
    icon: bi bi-globe
---
# docker stats

Zeige den Ressourcen-Verbrauch von Containern in Echtzeit.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/stats/>.

- Zeige sich stetig aktualisierende Statistiken von allen laufenden Containern:

`docker stats`

- Zeige sich stetig aktualisierende Statistiken der durch Leerzeichen getrennten Container:

`docker stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Ändere das Spaltenformat um die CPU Auslastung von Containern in Prozent anzuzeigen:

`docker stats --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Name</span>`:\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.CPUPerc</span>`"`

- Zeige Statistiken für alle Container (laufende und gestoppte):

`docker stats --all`

- Deaktiviere die laufende Aktualisierung und zeige nur die aktuellen Statistiken:

`docker stats --no-stream`
