---
layout: page
title: linux/tac (Nederlands)
description: "Toon en voeg bestanden samen met regels in omgekeerde volgorde."
content_hash: f8a47d20c311223e071a27cdcb4119dce78b798f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/tac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/tac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/tac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tac

Toon en voeg bestanden samen met regels in omgekeerde volgorde.
Bekijk ook: `cat`.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>.

- Voeg specifieke bestanden samen in omgekeerde volgorde:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Toon `stdin` in omgekeerde volgorde:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pad/naar/bestand</span>` | tac`

- Gebruik een specifiek scheidingsteken:

`tac --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Gebruik een specifieke regex als scheidingsteken:

`tac --regex --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[,;]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Gebruik een scheidingsteken vóór elk bestand:

`tac --before `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>
