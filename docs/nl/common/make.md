---
layout: page
title: common/make (Nederlands)
description: "Taakuitvoerder voor doelen beschreven in Makefile."
content_hash: 09258694b3a44446d83a5c5e7d774c161fd28252
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/make.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/make.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/make.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/make.html
    icon: bi bi-globe
tldri18n_status: 2
---
# make

Taakuitvoerder voor doelen beschreven in Makefile.
Wordt meestal gebruikt om de compilatie van een uitvoerbaar bestand uit broncode te beheren.
Meer informatie: <https://www.gnu.org/software/make/manual/make.html>.

- Roep het eerste doel aan dat in de Makefile is gespecificeerd (meestal "all" genoemd):

`make`

- Roep een specifiek doel aan:

`make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>

- Roep een specifiek doel aan en voer 4 taken tegelijk uit in parallel:

`make -j`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>

- Gebruik een specifieke Makefile:

`make --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Voer make uit vanuit een andere map:

`make --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Forceer het maken van een doel, zelfs als bronbestanden ongewijzigd zijn:

`make --always-make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>

- Overschrijf een variabele die in de Makefile is gedefinieerd:

`make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe_waarde</span>

- Overschrijf variabelen die in de Makefile zijn gedefinieerd door de omgeving:

`make --environment-overrides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>
