---
layout: page
title: common/pnmquant (Nederlands)
description: "Kwantiseer de kleuren in een PNM afbeelding naar een kleinere set."
content_hash: 3ca3e04f17ad2c67debda799fdf95d8a5d23f510
last_modified_at: 2023-12-22
related_topics:
  - title: English version
    url: /en/common/pnmquant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmquant

Kwantiseer de kleuren in een PNM afbeelding naar een kleinere set.
Dit commando is een combinatie van `pnmcolormap` en `pnmremap` en accepteert de combinatie van hun opties, behalve `-mapfile`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pnmquant.html>.

- Genereer een afbeelding door alleen gebruik te maken van `n_kleuren` of minder kleuren zo dichtbij mogelijk van de invoerafbeelding:

`pnmquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_kleuren</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>
