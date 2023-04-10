---
layout: page
title: common/node (italiano)
description: "Piattaforma JavaScript Server-side (Node.js)."
content_hash: a9b189874ab752ab99bf39150cadf784fbaf3486
last_modified_at: 2023-04-10
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
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/node.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
