---
layout: page
title: freebsd/df (Nederlands)
description: "Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte."
content_hash: 5230c6fb4c9059cf3d1792e9a37e8586f63e10a0
last_modified_at: 2024-01-09
related_topics:
  - title: English version
    url: /en/freebsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte.
Meer informatie: <https://man.freebsd.org/cgi/man.cgi?df>.

- Toon alle bestandssystemen en hun schijfgebruik met behulp van 512-byte eenheden:

`df`

- Gebruik leesbare eenheden (gebaseerd op de macht van 1024) en toon het grote totaal:

`df -h -c`

- Gebruik leesbare eenheden (gebaseerd op de macht van 1000):

`df -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-si|H</span>

- Toon het bestandssysteem en het schijfgebruik voor het opgegeven bestand of map:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Neem statistieken op over het aantal beschikbare en gebruikte [i]-knooppunten inclusief de bestandssysteem [T]ypes:

`df -iT`

- Gebruik 1024-byte eenheden voor het schrijven van de ruimte figuren:

`df -k`

- Toon informatie in een [P]ortable wijze:

`df -P`
