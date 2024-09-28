---
layout: page
title: common/docker-stats (Deutsch)
description: "Zeige den Ressourcen-Verbrauch von Containern in Echtzeit."
content_hash: 69b2f2638b5b1c1034e70d8a29733a63cd83b2c5
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/common/docker-stats.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-stats.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-stats.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-stats.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker stats

Zeige den Ressourcen-Verbrauch von Containern in Echtzeit.
Weitere Informationen: <https://docs.docker.com/reference/cli/docker/container/stats/>.

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
