---
layout: page
title: common/fc (Nederlands)
description: "Open het meest recente commando voor bewerking en voer het uit."
content_hash: ea6c1a1f781a4b19054db52d2fc6313c5ca4459a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/fc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fc.html
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

- Toon de help:

`fc --help`
