---
layout: page
title: sunos/prstat (Nederlands)
description: "Rapportering van de statistieken van actieve processen."
content_hash: 8808871e424e05a26f9a4be71a719d09f0dbd804
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prstat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># prstat

Rapportering van de statistieken van actieve processen.
Meer informatie: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Bekijken alle processen en rapporteer de statieken gestoord op basis van CPU gebruik:

`prstat`

- Bekijken alle processen en rapporteer de statieken gestoord op basis van geheugen gebruik:

`prstat -s rss`

- Bekijk het totaal gebruik voor elke gebruiker:

`prstat -t`

- Bekijk de microstate process accounting informatie:

`prstat -m`

- Print de 5 meest CPU intensieve processen elke seconde:

`prstat -c -n 5 -s cpu 1`
