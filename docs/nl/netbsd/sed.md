---
layout: page
title: netbsd/sed (Nederlands)
description: "Pas tekst aan in een op een scriptbare manier."
content_hash: 9e69140dfe36366118b9995207f4229f31a403c5
last_modified_at: 2024-01-08
related_topics:
  - title: English version
    url: /en/netbsd/sed.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/netbsd/sed.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sed

Pas tekst aan in een op een scriptbare manier.
Bekijk ook: `awk`, `ed`.
Meer informatie: <https://man.netbsd.org/sed.1>.

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in alle invoerregels en toon het resultaat in `stdout`::

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed 's/apple/mango/g'`

- Voer een specifiek script bestand uit en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sed</span>

- Vertraag het openen van elk bestand tot een commando met de gerelateerde `w`-functie of vlag wordt toegepast op een regel invoer:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sed</span>

- Turn on GNU re[g]ex extension:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sed</span>

- Vervang alle `apple` (uitgebreide regex) met `APPLE` (uitgebreide regex) in alle invoerregels en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -E 's/(apple)/\U\1/g'`

- Toon alleen de eerste regel in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -n '1p'`

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in een specifiek bestand en overschrijf het originele bestand:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
