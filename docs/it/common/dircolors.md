---
layout: page
title: common/dircolors (italiano)
description: "Stampa comandi necessari per settare la variabile d'ambiente LS_COLOR per stilizzare `ls`, `dir`, etc."
content_hash: 1f0f7b9ca9502a3431d97a16c26d02356987f270
last_modified_at: 2024-12-22
related_topics:
  - title: English version
    url: /en/common/dircolors.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dircolors.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/dircolors.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dircolors

Stampa comandi necessari per settare la variabile d'ambiente LS_COLOR per stilizzare `ls`, `dir`, etc.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

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
