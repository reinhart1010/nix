---
layout: page
title: linux/bspc (Nederlands)
description: "Een tool om `bspwm` te besturen."
content_hash: bedca1ea3d1602508bb4f5993522ebed89b5f1f6
last_modified_at: 2024-06-19
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

`bspc desktop --focus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nummer</span>

- Sluit de vensters die afgetakt zijn van de geselecteerde node:

`bspc node --close`

- Stuur de geselecteerde node naar het opgegeven bureaublad:

`bspc node --to-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nummer</span>

- Schakel de modus volledig scherm in voor de geselecteerde node:

`bspc node --state ~fullscreen`

- Zet de waarde van een specifieke instelling:

`bspc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instelling</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>
