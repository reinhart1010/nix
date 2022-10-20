---
layout: page
title: common/cloc (italiano)
description: "Conta e calcola le differenze di linee di codice sorgente e commenti."
content_hash: 96ff8582349677e0ad3c8777223437ed0425cd4b
related_topics:
  - title: English version
    url: /en/common/cloc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cloc.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cloc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cloc

Conta e calcola le differenze di linee di codice sorgente e commenti.
Maggiori informazioni: <https://github.com/AlDanial/cloc>.

- Conta tutte le linee di codice in una directory:

`cloc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Conta tutte le linee di codice in una directory, mostrando una barra di avanzamento durante l'operazione:

`cloc --progress=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Compara i file sorgente in 2 diverse directory e conta le differenze tra di essi:

`cloc --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory2</span>
