---
layout: page
title: common/nvim (italiano)
description: "Neovim, un editor di testo basato su Vim che offre molti diversi modi di manipolare e navigare il testo."
content_hash: 81862d5cacefee397ac62a5352523ef020b9df39
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/nvim.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/nvim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nvim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/nvim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvim

Neovim, un editor di testo basato su Vim che offre molti diversi modi di manipolare e navigare il testo.
Premere `i` per entrare in modalità inserimento (insert mode), `<Esc>` per uscire e tornare alla modalità normale (normal mode).
Maggiori informazioni: <https://neovim.io>.

- Aprire un file:

`nvim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Entrare nella modalità per scrivere testo (insert mode):

`<Esc>i`

- Copiare ("yank") o cancellare ("delete") la linea corrente (può poi essere copiata con `p` o `P`):

`<Esc>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yy|dd</span>

- Annullare l'ultima operazione fatta:

`<Esc>u`

- Cercare uno specifico pattern nel file (premere `n`/`N` per navigare tra le occorrenze successive/precedenti):

`<Esc>/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patter_da_cercare</span>`<Enter>`

- Eseguire una sostituzione tramite espressione regolare nell'intero file:

`<Esc>:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">espressione_regolare</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sostituzione</span>`/g<Enter>`

- Salvare (scrivere) il file per poi uscire:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><Esc>ZZ|<Esc>:wq<Enter></span>

- Uscire senza salvare:

`<Esc>:q!<Enter>`
