---
layout: page
title: common/tlmgr-platform (Nederlands)
description: "Beheer TeX Live platforms."
content_hash: 369cb57e045fe7a49cac02893fb4906999bf9331
last_modified_at: 2023-12-23
related_topics:
  - title: English version
    url: /en/common/tlmgr-platform.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr platform

Beheer TeX Live platforms.
Meer informatie: <https://www.tug.org/texlive/tlmgr.html>.

- Toon alle beschikbare platforms in een pakket repository:

`tlmgr platform list`

- Voeg de uitvoerbare bestanden toe aan een specifiek platform:

`sudo tlmgr platform add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>

- Verwijder de uitvoerbare bestanden uit een specifiek platform:

`sudo tlmgr platform remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>

- Detecteer automatisch en wissel naar het huidige platform:

`sudo tlmgr platform set auto`

- Wissel naar een specifiek platform:

`sudo tlmgr platform set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>
