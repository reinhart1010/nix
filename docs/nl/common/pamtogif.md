---
layout: page
title: common/pamtogif (Nederlands)
description: "Converteer een Netpbm afbeelding naar een ongeanimeerde GIF afbeelding."
content_hash: 10cbefe996843216c1ff41af69acbac972393e3a
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pamtogif.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pamtogif.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamtogif

Converteer een Netpbm afbeelding naar een ongeanimeerde GIF afbeelding.
Bekijk ook: `giftopnm`, `gifsicle`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamtogif.html>.

- Converteer een Netpbm afbeelding naar een ongeanimeerde GIF afbeelding:

`pamtogif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.gif</span>

- Markeer de gespecificeerde kleur als transparent in het uitvoer GIF bestand:

`pamtogif -transparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kleur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.gif</span>

- Voeg de gespecificeerde tekst toe als commentaar in het uitvoer GIF bestand:

`pamtogif -comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo Wereld!</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.gif</span>
