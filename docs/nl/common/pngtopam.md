---
layout: page
title: common/pngtopam (Nederlands)
description: "Converteer een PNG afbeelding naar een Netpbm afbeelding."
content_hash: 6003c7fbf322cbe1a7f1c4132c67572018ee95b9
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pngtopam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pngtopam

Converteer een PNG afbeelding naar een Netpbm afbeelding.
Bekijk ook: `pamtopng`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pngtopam.html>.

- Converteer de gespecificeerde PNG afbeelding naar een Netpbm afbeelding:

`pngtopam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Maak een uitvoerafbeelding die zowel de hoofdafbeelding als de transparantiemasker van de invoerafbeelding bevat:

`pngtopam -alphapam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Vervang transparente pixels door de gespecificeerde kleur:

`pngtopam -mix -background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kleur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Schrijf tEXt chunks gevonden in de invoer-afbeelding naar het gespecificeerde tekstbestand:

`pngtopam -text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>
