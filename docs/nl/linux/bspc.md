---
layout: page
title: linux/bspc (Nederlands)
description: "Een tool om `bspwm` te besturen."
content_hash: 64cba35b11c93f383fee8fe87160e55675216464
last_modified_at: 2024-03-09
related_topics:
  - title: English version
    url: /en/linux/bspc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bspc

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

- Zet de waarde van een specifieke instelling:

`bspc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instelling</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>
