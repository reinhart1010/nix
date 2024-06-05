---
layout: page
title: common/pnmcolormap (Nederlands)
description: "Maak een kwantisatiekleurkaart voor een PNM afbeelding."
content_hash: 2e13bafb2dac15db03838f66d6568561c3e77a21
last_modified_at: 2024-06-05
related_topics:
  - title: English version
    url: /en/common/pnmcolormap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmcolormap

Maak een kwantisatiekleurkaart voor een PNM afbeelding.
Meer informatie: <https://netpbm.sourceforge.net/doc/pnmcolormap.html>.

- Genereer een afbeelding met alleen `n_kleuren` of minder kleuren, zo dicht als mogelijk bij de invoer-afbeelding:

`pnmcolormap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_kleuren</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ppm</span>

- Gebruik de splitspread strategie voor het bepalen van de uitvoer-kleuren, welke waarschijnlijk een beter resultaat oplevert met afbeeldingen met kleine details:

`pnmcolormap -splitspread `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_kleuren</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ppm</span>

- Sorteer de resulteerde kleurkaart, welke nuttig is voor het vergelijken van kleurkaarten:

`pnmcolormap -sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ppm</span>
