---
layout: page
title: common/ect (italiano)
description: "Efficiente Tool di Compressione (o ECT) è un ottimizzatore di file scritto in C++. Supporta file PNG, JPEG, GZIP e ZIP."
content_hash: 18cef0d0e07848271516334d1bfb53ac721f7e00
related_topics:
  - title: English version
    url: /en/common/ect.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ect

Efficiente Tool di Compressione (o ECT) è un ottimizzatore di file scritto in C++. Supporta file PNG, JPEG, GZIP e ZIP.
Maggiori informazioni: <https://github.com/fhanau/Efficient-Compression-Tool>.

- Comprimi un file:

`ect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.png</span>

- Comprimi un file con il massimo livello di compressione utilizzanto più thread:

`ect -9 --mt-deflate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.png</span>

- Comprimi tutti i file in una directory ricorsivamente, mantenendo la data di modifica originale:

`ect -keep -recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/directory</span>
