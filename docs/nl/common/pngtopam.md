---
layout: page
title: common/pngtopam (Nederlands)
description: "Converteer een PNG afbeelding naar een Netpbm afbeelding."
content_hash: 6003c7fbf322cbe1a7f1c4132c67572018ee95b9
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pngtopam.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pngtopam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pngtopam

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
