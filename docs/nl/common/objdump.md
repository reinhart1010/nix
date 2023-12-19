---
layout: page
title: common/objdump (Nederlands)
description: "Bekijk informatie over object bestanden."
content_hash: 5a1ed94fe1d66ca94afc0a06741ead1e73c5a44e
last_modified_at: 2023-12-19
related_topics:
  - title: English version
    url: /en/common/objdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# objdump

Bekijk informatie over object bestanden.
Meer informatie: <https://manned.org/objdump>.

- Toon de bestand header informatie:

`objdump -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary</span>

- Toon alle header informatie:

`objdump -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary</span>

- Toon de gedemonteerde uitvoer van uitvoerbare secties:

`objdump -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary</span>

- Toon de gedemonteerde uitvoer van uitvoerbare secties in intel syntax:

`objdump -M intel -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary</span>

- Toon een complete binary hex dump van alle secties:

`objdump -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary</span>
