---
layout: page
title: common/seq (Nederlands)
description: "Toon een reeks getallen naar `stdout`."
content_hash: 4147824bab1d4f38939d11f42392a388538eb943
last_modified_at: 2024-06-28
related_topics:
  - title: English version
    url: /en/common/seq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/seq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># seq

Toon een reeks getallen naar `stdout`.
Meer informatie: <https://www.gnu.org/software/coreutils/seq>.

- Reeks van 1 tot 10:

`seq 10`

- Elk 3e nummer van 5 tot 20:

`seq 5 3 20`

- Scheid de uitvoer met een spatie in plaats van een nieuwe regel:

`seq -s " " 5 3 20`

- Formatteer de uitvoerbreedte naar minimaal 4 cijfers, opgevuld met nullen indien nodig:

`seq -f "%04g" 5 3 20`
