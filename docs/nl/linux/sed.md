---
layout: page
title: linux/sed (Nederlands)
description: "Pas tekst aan in een op een scriptbare manier."
content_hash: 6da5d14e3215b233e7bf42a1b3780b079f2b1056
last_modified_at: 2024-01-29
related_topics:
  - title: English version
    url: /en/linux/sed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Pas tekst aan in een op een scriptbare manier.
Bekijk ook: `awk`, `ed`.
Meer informatie: <https://www.gnu.org/software/sed/manual/sed.html>.

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in alle invoerregels en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed 's/apple/mango/g'`

- Vervang alle `apple` (uitgebreide regex) met `APPLE` (uitgebreide regex) in alle invoerregels en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -E 's/(apple)/\U\1/g'`

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in een specifiek bestand en overschrijf het originele bestand:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Voer een specifiek script bestand uit en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sed</span>

- Toon alleen de eerste regel in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -n '1p'`

- Verwijder de eerste regel van een bestand:

`sed -i 1d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Voeg een nieuwe regel in bij de eerste regel van een bestand:

`sed -i '1i\your new line text\' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
