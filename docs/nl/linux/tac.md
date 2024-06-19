---
layout: page
title: linux/tac (Nederlands)
description: "Toon en voeg bestanden samen met regels in omgekeerde volgorde."
content_hash: 64b3cd9ddd22c1f5db55272bd5b723c42cc440b6
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/linux/tac.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tac.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tac

Toon en voeg bestanden samen met regels in omgekeerde volgorde.
Bekijk ook: `cat`.
Meer informatie: <https://www.gnu.org/software/coreutils/tac>.

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
