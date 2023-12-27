---
layout: page
title: common/tac (italiano)
description: "Visualizza e concatena file con righe in ordine inverso."
content_hash: 4e7b46942d8623bd93f049ffa1972f1bd4ce9240
last_modified_at: 2023-12-27
related_topics:
  - title: English version
    url: /en/common/tac.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tac

Visualizza e concatena file con righe in ordine inverso.
Guarda anche: `cat`.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/tac>.

- Concatena file specifici in ordine inverso:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1 percorso/del/file2 ...</span>

- Visualizza 'stdin' in ordine inverso:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat percorso/del/file</span>` | tac`

- Usa un [s]riparatore specifico:

`tac -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">separatore</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1 percorso/del/file2 ...</span>

- Usa un [r]egex specifico come [s]eparatore:

`tac -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">separatore</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1 percorso/del/file2 ...</span>

- Utilizzare un separatore [b]prima di ciascun file:

`tac -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1 percorso/del/file2 ...</span>
