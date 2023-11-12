---
layout: page
title: common/node (italiano)
description: "Piattaforma JavaScript Server-side (Node.js)."
content_hash: a9b189874ab752ab99bf39150cadf784fbaf3486
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/node.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/node.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/node.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/node.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/node.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/node.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># node

Piattaforma JavaScript Server-side (Node.js).
Maggiori informazioni: <https://nodejs.org>.

- Esegue un file JavaScript:

`node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Avvia una REPL (shell interattiva):

`node`

- Esegue il codice JavaScript che viene specificato come argomento:

`node -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codice</span>`"`

- Valuta un'espressione e ne stampa il risultato, questo comando specifico è utile per vedere le versioni delle dipendenze di node:

`node -p "process.versions"`

- Attiva il debugger mettendo in pausa l'esecuzione finché il codice sorgente non viene caricato:

`node --no-lazy --inspect-brk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>
