---
layout: page
title: common/tac (italiano)
description: "Visualizza e concatena file con righe in ordine inverso."
content_hash: b9f370ff051e5e4aed342e6b0dea0c994f729a26
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tac

Visualizza e concatena file con righe in ordine inverso.
Guarda anche: `cat`.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>.

- Concatena file specifici in ordine inverso:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1 percorso/del/file2 ...</span>

- Visualizza `stdin` in ordine inverso:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat percorso/del/file</span>` | tac`

- Usa un [s]riparatore specifico:

`tac -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">separatore</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1 percorso/del/file2 ...</span>

- Usa un [r]egex specifico come [s]eparatore:

`tac -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">separatore</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1 percorso/del/file2 ...</span>

- Utilizzare un separatore [b]prima di ciascun file:

`tac -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1 percorso/del/file2 ...</span>
