---
layout: page
title: common/pamtopng (Nederlands)
description: "Converteer een PAM afbeelding naar PNG."
content_hash: e37c2e2d0ad6897a409e4d72345b3985a91505e1
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pamtopng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamtopng

Converteer een PAM afbeelding naar PNG.
Bekijk ook: `pnmtopng`, `pngtopam`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamtopng.html>.

- Converteer de gespecificeerde PAM afbeelding naar PNG:

`pamtopng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.png</span>

- Markeer de gespecificeerde kleur als transparent in de uitvoer-afbeelding:

`pamtopng -transparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kleur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.png</span>

- Voeg de tekst in gespecificeerde bestand toe als tEXt chunks in de uitvoer:

`pamtopng -text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.png</span>

- Zorg ervoor dat het uitvoerbestand geïnterlaced is in Adam7-formaat:

`pamtopng -interlace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.png</span>
