---
layout: page
title: osx/netstat (Nederlands)
description: "Toon netwerkgerelateerde informatie zoals open verbindingen, open socketpoorten, enz."
content_hash: 199f055b5ceba133c41930371018ac44d3dd87c5
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/osx/netstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/osx/netstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netstat

Toon netwerkgerelateerde informatie zoals open verbindingen, open socketpoorten, enz.
Bekijk ook: `lsof` voor het weergeven van netwerkverbindingen, inclusief luisterpoorten.
Meer informatie: <https://keith.github.io/xcode-man-pages/netstat.1.html>.

- Toon de PID en programmanaam die luistert op een specifiek protocol:

`netstat -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol</span>

- Toon de routeringstabel en los IP-adressen niet op naar hostnamen:

`netstat -nr`

- Toon de routeringstabel van IPv4-adressen:

`netstat -nr -f inet`
