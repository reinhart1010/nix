---
layout: page
title: common/fc (Nederlands)
description: "Open het meest recente commando voor bewerking en voer het uit."
content_hash: 2797568703df369ca75a9ca06fb6f0be5b628a06
last_modified_at: 2024-10-09
related_topics:
  - title: English version
    url: /en/common/fc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fc

Open het meest recente commando voor bewerking en voer het uit.
Meer informatie: <https://manned.org/fc>.

- Open het laatste commando in de standaard systeemeditor en voer het uit na het aanpassen:

`fc`

- Specificeer een editor om mee te openen:

`fc -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'emacs'</span>

- Toon recente commando's uit de geschiedenis:

`fc -l`

- Toon recente commando's in omgekeerde volgorde:

`fc -l -r`

- Pas een commando uit de geschiedenis aan en voer het uit:

`fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nummer</span>

- Pas commando's in een gegeven interval aan en voer ze uit:

`fc '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">416</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">420</span>`'`

- Toon help:

`fc --help`
