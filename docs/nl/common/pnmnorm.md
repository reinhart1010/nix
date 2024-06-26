---
layout: page
title: common/pnmnorm (Nederlands)
description: "Normaliseer het contrast in een PNM afbeelding."
content_hash: d0707703c3f17f5fa5f04695a0761d4ece3a27ff
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pnmnorm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmnorm

Normaliseer het contrast in een PNM afbeelding.
Bekijk ook: `pnmhisteq`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pnmnorm.html>.

- Forceer de helderste pixels om wit te zijn, de donkerste pixels om zwart te zijn en verspreid de tussenliggende pixels lineair:

`pnmnorm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>

- Forceer de helderste pixels om wit te zijn, de donkerste pixels om zwart te zijn en verspreid de tussenliggende pixels kwadratisch zodat pixels met een helderheid van `n` 50% helderder worden:

`pnmnorm -midvalue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>

- Behoud de tint van de pixels, pas alleen de helderheid aan:

`pnmnorm -keephues `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>

- Specificeer een methode om de helderheid van een pixel te berekenen:

`pnmnorm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">luminosity|colorvalue|saturation</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>
