---
layout: page
title: common/pamcut (Nederlands)
description: "Snij een rechthoekig gebied uit van een Netpbm afbeelding."
content_hash: 93e2856234a241b7d528dd1e0e510310e7d66b06
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pamcut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamcut

Snij een rechthoekig gebied uit van een Netpbm afbeelding.
Bekijk ook: `pamcrop`, `pamdice`, `pamcomp`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamcut.html>.

- Verwijder het gespecificeerde nummer van kolommen/rijen van iedere zijde van de afbeelding:

`pamcut -cropleft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` -cropright `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` -croptop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` -cropbottom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ppm</span>

- Behoud alleen de kolommen tussen de gespecificeerde kolommen (inclusief de gespecificeerde):

`pamcut -left `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` -right `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ppm</span>

- Vul missende gebieden met zwarte pixels als de gespecificeerde rechthoek niet volledig ligt in de invoer-afbeelding:

`pamcut -top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` -bottom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` -pad `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ppm</span>
