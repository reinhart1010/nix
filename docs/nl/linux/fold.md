---
layout: page
title: linux/fold (Nederlands)
description: "Breek lange regels af voor uitvoerapparaten met vaste breedte."
content_hash: e564b080e120a77310cc3260a6311eb8502853d1
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/fold.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/fold.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fold

Breek lange regels af voor uitvoerapparaten met vaste breedte.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/fold-invocation.html>.

- Breek regels af met een vaste breedte:

`fold --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">breedte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Tel breedte in bytes (standaard is het tellen in kolommen):

`fold --bytes --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">breedte_in_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Breek de regel na de meest rechtse spatie binnen de breedtelimiet:

`fold --spaces --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">breedte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
