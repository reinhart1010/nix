---
layout: page
title: common/sed (Nederlands)
description: "Pas tekst aan in een op een scriptbare manier."
content_hash: ff0e1b25e186b9984dc94999baebf6af841d7fe2
last_modified_at: 2024-06-13
related_topics:
  - title: dansk version
    url: /da/common/sed.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sed.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Pas tekst aan in een op een scriptbare manier.
Bekijk ook: `awk`, `ed`.
Meer informatie: <https://manned.org/sed.1posix>.

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in alle invoerregels en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed 's/apple/mango/g'`

- Voer een specifiek script bestand uit en toon het resultaat in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sed</span>

- Toon alleen de eerste regel in `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sed -n '1p'`
