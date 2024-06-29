---
layout: page
title: common/tsort (Nederlands)
description: "Voer een topologische sortering uit."
content_hash: 8f1b05dc186c6f965872a6579468d0944f7dc441
last_modified_at: 2024-06-29
related_topics:
  - title: English version
    url: /en/common/tsort.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tsort

Voer een topologische sortering uit.
Een veelvoorkomend gebruik is om de afhankelijkheidsvolgorde van knooppunten in een gerichte acyclische grafiek te tonen.
Meer informatie: <https://www.gnu.org/software/coreutils/tsort>.

- Voer een topologische sortering uit consistent met een gedeeltelijke sortering per regel van invoer gescheiden door spaties:

`tsort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Voer een topologische sortering uit consistent op strings:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UI Backend\nBackend Database\nDocs UI</span>`" | tsort`
