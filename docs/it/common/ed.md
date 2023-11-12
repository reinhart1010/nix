---
layout: page
title: common/ed (italiano)
description: "L'originale editor di testo Unix."
content_hash: 9e66b174b173a86ee2cdae846a0356c33cef978c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ed.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ed

L'originale editor di testo Unix.
Maggiori informazioni: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Avvia ed per editare un documento vuoto (che può essere salvato come nuovo file nella directory corrente):

`ed`

- Avvia ed per editare un documento vuoto, con `:` come indicatore del prompt di comandi:

`ed -p :`

- Avvia ed per editare un file esistente (mostra il numero di byte del file caricato):

`ed -p : `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Attiva o disattiva la stampa di spiegazioni per gli errori (di default, le spiegazioni non sono stampate ed appare solo un `?`):

`H`

- Aggiungi del testo al documento corrente. Indica il completamento inserendo un punto da solo su una nuova linea:

`a<Enter>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text_to_insert</span>`<Enter>.`

- Stampa l'intero documento (`,` è una scorciatoia per il range `1,$` che copre dall'inizio alla fine del documento):

`,p`

- Scrivi il documento corrente su un nuovo file (il nome del file può essere omesso se `ed` è stato avviato con un file esistente):

`w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Termina ed:

`q`
