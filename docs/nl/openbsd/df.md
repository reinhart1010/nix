---
layout: page
title: openbsd/df (Nederlands)
description: "Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte."
content_hash: 84cccbf128d15a06cb76220ec37706018eb291e9
last_modified_at: 2024-01-09
related_topics:
  - title: English version
    url: /en/openbsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte.
Meer informatie: <https://man.openbsd.org/df.1>.

- Toon alle bestandssystemen en hun schijfgebruik met behulp van 512-byte eenheden:

`df`

- Toon alle bestandssystemen en hun schijfgebruik in een leesbaar formaat (gebaseerd op de macht van 1024):

`df -h`

- Toon het bestandssysteem en het schijfgebruik voor het opgegeven bestand of map:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Neem statistieken op over het aantal beschikbare en gebruikte [i]-knooppunten:

`df -i`

- Gebruik 1024-byte eenheden voor het schrijven van de ruimte figuren:

`df -k`

- Toon informatie in een [P]ortable wijze:

`df -P`
