---
layout: page
title: common/egrep (Nederlands)
description: "Vind patronen in bestanden door gebruik te maken van uitgebreidere reguliere expressies (ondersteund `?`, `+`, `{}`, `()` en `|`)."
content_hash: 21ac1b7943d411cbe6b2af148d41becb7eab070a
last_modified_at: 2024-02-01
related_topics:
  - title: English version
    url: /en/common/egrep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/egrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# egrep

Vind patronen in bestanden door gebruik te maken van uitgebreidere reguliere expressies (ondersteund `?`, `+`, `{}`, `()` en `|`).
Meer informatie: <https://manned.org/egrep>.

- Zoek naar een patroon in een bestand:

`egrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zoek naar een patroon in meerdere bestanden:

`egrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Zoek in `stdin` naar een patroon:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | egrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>

- Toon de bestandsnaam en het regelnummer voor iedere overeenkomst:

`egrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zoek recursief in alle bestanden in een map voor een patroon, maar negeer binaire bestanden:

`egrep --recursive --binary-files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">without-match</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Zoek voor regels die niet voldoen aan een patroon:

`egrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
