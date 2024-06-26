---
layout: page
title: common/pamslice (Nederlands)
description: "Haal een regel van waarden uit een PAM afbeelding."
content_hash: 1942f2132fd21a52f94e6e4370a8b83e682c2c61
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pamslice.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pamslice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamslice

Haal een regel van waarden uit een PAM afbeelding.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamslice.html>.

- Toon de waarden van de pixels in de opgegeven rij in een tabel:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>

- Toon de waarden van de pixels in de opgegeven kolom in een tabel:

`pamslice -column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>

- Beschouw alleen het opgegeven vlak (m) van de invoer-afbeelding:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -plane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>

- Produceer uitvoer in een formaat dat geschikt is voor invoer naar een `xmgr` voor visualisatie:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -xmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>
