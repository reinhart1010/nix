---
layout: page
title: osx/shuf (Nederlands)
description: "Genereer willekeurige permutaties."
content_hash: 940367209cabff4c90f5594a9c73d2b6d1675b02
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/shuf.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/shuf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/shuf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/shuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shuf

Genereer willekeurige permutaties.
Meer informatie: <https://keith.github.io/xcode-man-pages/shuf.1.html>.

- Wijzig willekeurig de volgorde van regels in een bestand en toon het resultaat:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon alleen de eerste 5 regels van het resultaat:

`shuf --head-count=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Schrijf de uitvoer naar een ander bestand:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand</span>

- Genereer willekeurige getallen in het bereik van 1 tot 10:

`shuf --input-range=1-10`
