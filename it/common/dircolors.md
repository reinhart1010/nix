---
layout: page
title: common/dircolors (italiano)
description: "Stampa comandi necessari per settare la variabile d'ambiente LS_COLOR per stilizzare `ls`, `dir`, etc."
content_hash: 949506bf245f05a1279d1b2f954a0c095175a01f
related_topics:
  - title: English version
    url: /en/common/dircolors.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dircolors.html
    icon: bi bi-globe
---
# dircolors

Stampa comandi necessari per settare la variabile d'ambiente LS_COLOR per stilizzare `ls`, `dir`, etc.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/dircolors>.

- Stampa i comandi per settare LS_COLOR con i colori predefiniti:

`dircolors`

- Stampa i comandi per settare LS_COLOR con i colori definiti in un file:

`dircolors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Stampa comandi per la Bourne shell:

`dircolors --bourne-shell`

- Stampa comandi per la C shell:

`dircolors --c-shell`

- Mostra i colori predefiniti per diversi tipi di file ed estensioni:

`dircolors --print-data`
