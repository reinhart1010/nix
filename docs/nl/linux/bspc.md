---
layout: page
title: linux/bspc (Nederlands)
description: "Een tool om `bspwm` te besturen."
content_hash: 5bee8413cd24f9ba045acaea266dab83c542cfb2
last_modified_at: 2023-10-20
related_topics:
  - title: English version
    url: /en/linux/bspc.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bspc

Een tool om `bspwm` te besturen.
Meer informatie: <https://github.com/baskerville/bspwm>.

- Definieer twee virtuele bureaubladen:

`bspc monitor --reset-desktops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Focus op het gegeven bureaublad:

`bspc desktop --focus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Sluit de vensters die afgetakt zijn van het geselecteerde knooppunt:

`bspc node --close`

- Stuur het geselecteerde knooppunt naar het opgegeven bureaublad:

`bspc node --to-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Schakel de modus volledig scherm in voor het geselecteerde knooppunt:

`bspc node --state ~fullscreen`
