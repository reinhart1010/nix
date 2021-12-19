---
layout: page
title: common/nvim (italiano)
description: "Neovim, un editor di testo basato su Vim che offre molti diversi modi di manipolare e navigare il testo."
content_hash: bd1600ee6ac51478837fd97eb3c4ff51a1cd8846
related_topics:
  - title: English version
    url: /en/common/nvim.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/nvim.html
    icon: bi bi-globe
---
# nvim

Neovim, un editor di testo basato su Vim che offre molti diversi modi di manipolare e navigare il testo.
Premere `i` per entrare in modalità inserimento (insert mode), `<Esc>` per uscire e tornare alla modalità normale (normal mode).
Maggiori informazioni: <https://neovim.io>.

- Aprire un file:

`nvim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Entrare nella modalità per scrivere testo (insert mode):

`<Esc>i`

- Copiare ("yank") o cancellare ("delete") la linea corrente (può poi essere copiara con `p` o `P`):

`<Esc>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yy|dd</span>

- Annullare l'ultima operazione fatta:

`<Esc>u`

- Cercare uno specifico pattern nel file (premere `n`/`N` per navigare tra le occorrenze successive/precedenti):

`<Esc>/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patter_da_cercare</span>`<Enter>`

- Eseguire una sostituzione tramite espressione regolare nell'intero file:

`<Esc>:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">espressione_regolare</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sostituzione</span>`//g<Enter>`

- Salvare (scrivere) il file per poi uscire:

`<Esc>:wq<Enter>`

- Uscire senza salvare:

`<Esc>:q!<Enter>`
