---
layout: page
title: common/readlink (italiano)
description: "Segue un collegamento simbolico e ne recupera le informazioni."
content_hash: 59ddcb5eab1604d517814b5b5d4481ab3afc70e3
related_topics:
  - title: English version
    url: /en/common/readlink.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># readlink

Segue un collegamento simbolico e ne recupera le informazioni.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/readlink>.

- Restituisce il percorso originale a cui il collegamento simbolico fa riferimento:

`readlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Ottiene il percorso assoluto di un file:

`readlink -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>
