---
layout: page
title: common/enscript (italiano)
description: "Converti file di testo in PostScript, HTML, RTF, ANSI ed overstrike."
content_hash: 03d06bb7b63afe08215518e8aef16fce3514fe51
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/enscript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# enscript

Converti file di testo in PostScript, HTML, RTF, ANSI ed overstrike.
Maggiori informazioni: <https://www.gnu.org/software/enscript>.

- Genera un file PostScript da un file di testo:

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_input</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Genera un file in un linguaggio differente da PostScript:

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_input</span>` --language=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linguaggio</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Genera un file PostScript con layout orizzontale, dividendo la pagina in colonne (massimo 9):

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_input</span>` --columns=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_colonne</span>` --landscape --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Mostra linguaggi e formati file disponibili per evidenziare la sintassi:

`enscript --help-highlight`

- Genera un file PostScript con evidenziazione della sintassi e colori per uno specifico linguaggio:

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_input</span>` --color=1 --highlight=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linguaggio</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>
