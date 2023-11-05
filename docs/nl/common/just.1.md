---
layout: page
title: common/just.1 (Nederlands)
description: "Sla op en run project-specifieke commands uit."
content_hash: 70ba8f318c694b183ca6c9dbc6f0a1f44fe6c250
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/common/just.1.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># just

Sla op en run project-specifieke commands uit.
Meer informatie: <https://github.com/casey/just>.

- Voer een recept uit dat gespecificeerd is in een justfile:

`just `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recept</span>

- Initialiseer nieuwe justfile in de beginmap van het project:

`just --init`

- Pas de justfile aan in de standaard tekstbewerker:

`just -e`

- Toon een lijst met beschikbare recepten in de justfile:

`just -l`

- Print de justfile:

`just --dump`
