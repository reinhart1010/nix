---
layout: page
title: common/shuf (Nederlands)
description: "Genereer willekeurige permutaties."
content_hash: dd89ba18c36dfc03016cd3508aec9f8715990e5e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/shuf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/shuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shuf

Genereer willekeurige permutaties.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/shuf-invocation.html>.

- Wijzig willekeurig de volgorde van regels in een bestand en toon het resultaat:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon alleen de eerste 5 regels van het resultaat:

`shuf --head-count=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Schrijf de uitvoer naar een ander bestand:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand</span>

- Genereer 3 willekeurige getallen in het bereik van 1 tot 10 (inclusief):

`shuf --head-count=3 --input-range=1-10 --repeat`
