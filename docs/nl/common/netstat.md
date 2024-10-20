---
layout: page
title: common/netstat (Nederlands)
description: "Toon netwerkgerelateerde informatie zoals open verbindingen, open socketpoorten, enz."
content_hash: 24c9dd590ad496e64aa401ad65d44c88a6d7c8c8
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/netstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/netstat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/netstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netstat

Toon netwerkgerelateerde informatie zoals open verbindingen, open socketpoorten, enz.
Meer informatie: <https://manned.org/netstat>.

- Toon alle poorten:

`netstat --all`

- Toon alle luisterende poorten:

`netstat --listening`

- Toon luisterende TCP-poorten:

`netstat --tcp`

- Toon PID en programmanamen:

`netstat --program`

- Toon informatie continu:

`netstat --continuous`

- Toon routes en los IP-adressen niet op naar hostnamen:

`netstat --route --numeric`

- Toon luisterende TCP- en UDP-poorten (+ gebruiker en proces als je root bent):

`netstat --listening --program --numeric --tcp --udp --extend`
