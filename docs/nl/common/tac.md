---
layout: page
title: common/tac (Nederlands)
description: "Toon en voeg bestanden samen met regels in omgekeerde volgorde."
content_hash: be9b1d82595f516841d6ffe6dee573c3ee690e1c
last_modified_at: 2024-06-20
related_topics:
  - title: English version
    url: /en/common/tac.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/tac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tac

Toon en voeg bestanden samen met regels in omgekeerde volgorde.
Bekijk ook: `cat`.
Meer informatie: <https://www.gnu.org/software/coreutils/tac>.

- Voeg specifieke bestanden samen in omgekeerde volgorde:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Toon `stdin` in omgekeerde volgorde:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pad/naar/bestand</span>` | tac`

- Gebruik een specifiek [s]cheidingsteken:

`tac -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheidingsteken</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Gebruik een specifieke [r]egex als [s]cheidingsteken:

`tac -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheidingsteken</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Gebruik een scheidingsteken vóór ([b]) elk bestand:

`tac -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>
