---
layout: page
title: common/cloc (italiano)
description: "Conta e calcola le differenze di linee di codice sorgente e commenti."
content_hash: 96ff8582349677e0ad3c8777223437ed0425cd4b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cloc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cloc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cloc

Conta e calcola le differenze di linee di codice sorgente e commenti.
Maggiori informazioni: <https://github.com/AlDanial/cloc>.

- Conta tutte le linee di codice in una directory:

`cloc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Conta tutte le linee di codice in una directory, mostrando una barra di avanzamento durante l'operazione:

`cloc --progress=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Compara i file sorgente in 2 diverse directory e conta le differenze tra di essi:

`cloc --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory2</span>
