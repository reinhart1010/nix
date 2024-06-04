---
layout: page
title: common/pnmquantall (Nederlands)
description: "Voer `pnmquant` tegelijk uit op meerdere bestanden zodat deze een kleurkaart delen."
content_hash: f0c84e5e952fbd9d3ade757cb852225dd757e96f
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pnmquantall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmquantall

Voer `pnmquant` tegelijk uit op meerdere bestanden zodat deze een kleurkaart delen.
Bekijk ook: `pnmquant`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pnmquantall.html>.

- Voer `pnmquant` uit op meerdere bestanden met de gespecificeerde parameters en overschrijf de originele bestanden:

`pnmquantall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_kleuren</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer1.pnm pad/naar/invoer2.pnm ...</span>

- Sla de gekwantificeerde afbeeldingen op naar bestanden met dezelfde namen als de invoerbestanden, maar met de gespecificeerde extensie:

`pnmquantall -ext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extensie</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_kleuren</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer1.pnm pad/naar/invoer2.pnm ...</span>
