---
layout: page
title: common/ed (italiano)
description: "L'originale editor di testo Unix."
content_hash: 1aa02df567cad38bb49aac79bd85f6240b32d64b
related_topics:
  - title: English version
    url: /en/common/ed.html
    icon: bi bi-globe
---
# ed

L'originale editor di testo Unix.
Maggiori informazioni: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Avvia ed per editare un documento vuoto (che può essere salvato come nuovo file nella directory corrente):

`ed`

- Avvia ed per editare un documento vuoto, con `:` come indicatore del prompt di comandi:

`ed -p :`

- Avvia ed per editare un file esistente (mostra il numero di byte del file caricato):

`ed -p : `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

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
