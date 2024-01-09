---
layout: page
title: osx/sed (Nederlands)
description: "Pas tekst aan in een op een scriptbare manier."
content_hash: 1d434dfa1700abc6ba2e42297a3b7944a30a9a1f
last_modified_at: 2024-01-09
related_topics:
  - title: English version
    url: /en/osx/sed.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/sed.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Pas tekst aan in een op een scriptbare manier.
Bekijk ook: `awk`, `ed`.
Meer informatie: <https://keith.github.io/xcode-man-pages/sed.1.html>.

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in alle invoerregels en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed 's/apple/mango/g'`

- Voer een specifiek script bestand uit en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script_file.sed</span>

- Vervang alle `apple` (uitgebreide regex) met `APPLE` (uitgebreide regex) in alle invoerregels en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -E 's/(apple)/\U\1/g'`

- Toon alleen de eerste regel in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -n '1p'`

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in een specifiek `bestand` en sla een backup op van het origineel in `bestand.bak`:

`sed -i bak 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
