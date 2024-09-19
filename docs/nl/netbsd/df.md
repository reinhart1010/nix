---
layout: page
title: netbsd/df (Nederlands)
description: "Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte."
content_hash: 9f16db59dd17c9228e4abf9597db1973bedb1653
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/netbsd/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte.
Meer informatie: <https://man.netbsd.org/df.1>.

- Toon alle bestandssystemen en hun schijfgebruik met behulp van 512-byte eenheden:

`df`

- Gebruik leesbare eenheden (gebaseerd op de macht van 1024):

`df -h`

- Toon alle velden van de structu(u)r(en) geretourneerd door `statvfs`:

`df -G`

- Toon het bestandssysteem en het schijfgebruik voor het opgegeven bestand of map:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Neem statistieken op over het aantal beschikbare en gebruikte [i]-knooppunten:

`df -i`

- Gebruik 1024-byte eenheden voor het schrijven van de ruimte figuren:

`df -k`

- Toon informatie in een [P]ortable wijze:

`df -P`
