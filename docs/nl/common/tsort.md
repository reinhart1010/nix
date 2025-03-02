---
layout: page
title: common/tsort (Nederlands)
description: "Voer een topologische sortering uit."
content_hash: df965258bd74a31ef19b62ac60a6f43f7e0f29ee
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tsort.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tsort.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tsort

Voer een topologische sortering uit.
Een veelvoorkomend gebruik is om de afhankelijkheidsvolgorde van knooppunten in een gerichte acyclische grafiek te tonen.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/tsort-invocation.html>.

- Voer een topologische sortering uit consistent met een gedeeltelijke sortering per regel van invoer gescheiden door spaties:

`tsort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Voer een topologische sortering uit consistent op strings:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UI Backend\nBackend Database\nDocs UI</span>`" | tsort`
