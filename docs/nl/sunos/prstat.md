---
layout: page
title: sunos/prstat (Nederlands)
description: "Rapportering van de statistieken van actieve processen."
content_hash: 37dbbf7f894a6dc9c08fecedf7c325bb00b210ee
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prstat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prstat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prstat.html
    icon: bi bi-globe
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

- Print de 5 meest CPU intensieve processen elke seconde:

`prstat -c -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -s cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
