---
layout: page
title: common/vim (italiano)
description: "Vi IMproved, un editor di testo per programmatori che fornisce diverse modalità per modificare testo."
content_hash: b8da299a04eeb87b05403be2f3d3b2cb9cdf9eab
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
---
# vim

Vi IMproved, un editor di testo per programmatori che fornisce diverse modalità per modificare testo.
Premi `i` per entrare in insert mode e `<Esc>` per tornare in normal mode dove non puoi inserire testo normalmente.
Maggiori informazioni: <https://www.vim.org>.

- Apri un file in vim:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Vai in insert mode (per inserire testo):

`<Esc>i`

- Copia ("yank") o taglia ("delete") la linea corrente (per incollarla poi con `P`):

`<Esc>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yy|dd</span>

- Annulla l'ultima operazione:

`<Esc>u`

- Cerca un pattern nel file (usa `n`/`N` per spostarti al risultato successivo/precedente):

`<Esc>/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">espressione_regolare</span>`<Invio>`

- Effettua una sostituzione tramite espressione regolare nell'intero file:

`<Esc>:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">espressione_regolare</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sostituzione</span>`/g<Invio>`

- Salva modifiche al file ed esci:

`<Esc>:wq<Invio>`

- Esci senza salvare:

`<Esc>:q!<Invio>`
