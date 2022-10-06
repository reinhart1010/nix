---
layout: page
title: sunos/svcs (Nederlands)
description: "Geef informatie over actieve services."
content_hash: a294d8e1a4c7c69a2e53ae59e54d2988c0ca7d7e
related_topics:
  - title: English version
    url: /en/sunos/svcs.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcs.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># svcs

Geef informatie over actieve services.
Meer informatie: <https://www.unix.com/man-page/linux/1/svcs>.

- Oplijsting van alle actieve services:

`svcs`

- Oplijsting van alle inactieve services:

`svcs -vx`

- Geef informatie over een specifieke service:

`svcs apache`

- Toon de locatie van de log file van een service:

`svcs -L apache`

- Toon de laatste lijnen van een service log file:

`tail $(svcs -L apache)`
