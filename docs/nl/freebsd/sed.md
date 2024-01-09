---
layout: page
title: freebsd/sed (Nederlands)
description: "Pas tekst aan in een op een scriptbare manier."
content_hash: 715c9089d4e0f3e56714dcc28caeae31425335c1
last_modified_at: 2024-01-09
related_topics:
  - title: English version
    url: /en/freebsd/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Pas tekst aan in een op een scriptbare manier.
Bekijk ook: `awk`, `ed`.
Meer informatie: <https://www.freebsd.org/cgi/man.cgi?sed>.

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in alle invoerregels en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed 's/apple/mango/g'`

- Voer een specifiek script bestand uit en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sed</span>

- Vertraag het openen van elk bestand tot een commando met de gerelateerde `w`-functie of vlag wordt toegepast op een regel invoer:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sed</span>

- Vervang alle `apple` (uitgebreide regex) met `APPLE` (uitgebreide regex) in alle invoerregels en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -E 's/(apple)/\U\1/g'`

- Toon alleen de eerste regel in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -n '1p'`

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in een specifiek bestand en overschrijf het originele bestand:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
