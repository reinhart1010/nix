---
layout: page
title: common/ect (italiano)
description: "Efficiente Tool di Compressione (o ECT) è un ottimizzatore di file scritto in C++. Supporta file PNG, JPEG, GZIP e ZIP."
content_hash: 376a84b322f8c6d3a8401352b143a86d18a11ecd
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ect.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ect.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ect

Efficiente Tool di Compressione (o ECT) è un ottimizzatore di file scritto in C++. Supporta file PNG, JPEG, GZIP e ZIP.
Maggiori informazioni: <https://github.com/fhanau/Efficient-Compression-Tool>.

- Comprimi un file:

`ect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.png</span>

- Comprimi un file con il massimo livello di compressione utilizzando più thread:

`ect -9 --mt-deflate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.png</span>

- Comprimi tutti i file in una directory ricorsivamente, mantenendo la data di modifica originale:

`ect -keep -recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>
