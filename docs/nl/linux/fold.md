---
layout: page
title: linux/fold (Nederlands)
description: "Breek lange regels af voor uitvoerapparaten met vaste breedte."
content_hash: 565bc7c09252db9f60099d19f9f08c028f71078f
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/linux/fold.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fold.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fold

Breek lange regels af voor uitvoerapparaten met vaste breedte.
Meer informatie: <https://www.gnu.org/software/coreutils/fold>.

- Breek regels af met een vaste breedte:

`fold --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">breedte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Tel breedte in bytes (standaard is het tellen in kolommen):

`fold --bytes --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">breedte_in_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Breek de regel na de meest rechtse spatie binnen de breedtelimiet:

`fold --spaces --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">breedte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
