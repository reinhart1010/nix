---
layout: page
title: linux/df (Nederlands)
description: "Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte."
content_hash: 2a017c976fccb692cc06ab3cf8e5a6354df35585
last_modified_at: 2024-01-09
related_topics:
  - title: English version
    url: /en/linux/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte.
Meer informatie: <https://www.gnu.org/software/coreutils/df>.

- Toon alle bestandssystemen en hun schijfgebruik:

`df`

- Toon alle bestandssystemen en hun schijfgebruik in een leesbaar formaat:

`df -h`

- Toon het bestandssysteem en het schijfgebruik voor het opgegeven bestand of map:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Neem statistieken op over het aantal beschikbare [i]-knooppunte:

`df -i`

- Toon bestandssystemen maar negeer specifieke types:

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
