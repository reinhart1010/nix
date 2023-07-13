---
layout: page
title: common/babeld (Deutsch)
description: "Routing-Daemon für Babel, der Firewall-ähnliche Filter benutzt."
content_hash: b5fcff42380fdc192ebc5976037c3b34fb37c906
last_modified_at: 2023-07-13
related_topics:
  - title: English version
    url: /en/common/babeld.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># babeld

Routing-Daemon für Babel, der Firewall-ähnliche Filter benutzt.
Weitere Informationen: <https://www.irif.fr/~jch/software/babel/babeld.html>.

- Starte `babeld` mit einer bestimmten Konfigurationsdatei:

`babeld -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/babeld.conf</span>

- Starte `babeld` mit mehreren Konfigurationsdateien (in der Reihenfolge des Einlesens):

`babeld -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ports.conf</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/filters.conf</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/interfaces.conf</span>

- Starte `babeld` als Daemon:

`babeld -D`

- Starte `babeld` und übergib einen Konfigurationsbefehl:

`babeld -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'redistribute metric 256'</span>

- Starte `babeld` und gib an, auf welchen Schnittstellen gearbeitet werden soll:

`babeld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>
