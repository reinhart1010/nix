---
layout: page
title: sunos/prstat (Nederlands)
description: "Rapportering van de statistieken van actieve processen."
content_hash: 0bb0012a0ee864beb1ffd982a889ebf253288ced
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prstat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/prstat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/prstat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prstat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prstat

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

- Toon de 5 meest CPU intensieve processen elke seconde:

`prstat -c -n 5 -s cpu 1`
