---
layout: page
title: common/indent (Nederlands)
description: "Wijzig het uiterlijk van een C/C++-programma door spaties in te voegen of te verwijderen."
content_hash: e4f0808529d7d3cbb95795499ddfe4a75fb6bcc6
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/indent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# indent

Wijzig het uiterlijk van een C/C++-programma door spaties in te voegen of te verwijderen.
Meer informatie: <https://www.gnu.org/software/indent/>.

- Formatteer C/C++-broncode volgens de Linux style guide, maak automatisch een back-up van de originele bestanden en vervang deze door de ingesprongen versies:

`indent --linux-style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/andere_bron.c</span>

- Formatteer C/C++-broncode volgens de GNU-stijl en sla de ingesprongen versie op in een ander bestand:

`indent --gnu-style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/indented_source.c</span>

- Formatteer C/C++-broncode volgens de stijl van Kernighan & Ritchie (K&R), geen tabs, 3 spaties per inspringing en breek regels af op 120 tekens:

`indent --k-and-r-style --indent-level3 --no-tabs --line-length120 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/indented_source.c</span>
