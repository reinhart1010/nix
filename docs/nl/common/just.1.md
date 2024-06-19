---
layout: page
title: common/just.1 (Nederlands)
description: "Sla op en run project-specifieke commands uit."
content_hash: 213fbb8b00aee977264de51280426a9b65114bcc
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/just.1.html
    icon: bi bi-globe
tldri18n_status: 2
---
# just

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

- Toon de justfile:

`just --dump`
