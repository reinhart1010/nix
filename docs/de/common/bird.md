---
layout: page
title: common/bird (Deutsch)
description: "BIRD Internet Routing Daemon."
content_hash: 19d3a178cd6acf1a02d8d0668224ea6b7c3c8875
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bird.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bird

BIRD Internet Routing Daemon.
Routing-Daemon mit Unterstützung für BGP, OSPF, Babel und weitere.
Weitere Informationen: <https://bird.network.cz/>.

- Starte `bird` mit einer bestimmten Konfigurationsdatei:

`bird -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bird.conf</span>

- Starte `bird` als spezifischer Benutzer und Gruppe:

`bird -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppe</span>
