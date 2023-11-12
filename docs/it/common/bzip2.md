---
layout: page
title: common/bzip2 (italiano)
description: "Compressore di file a blocchi ordinati."
content_hash: fe32228a908ac6fa5f1abe641980031ee4c3734e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bzip2.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bzip2.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bzip2.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bzip2

Compressore di file a blocchi ordinati.
Maggiori informazioni: <https://manned.org/bzip2>.

- Comprimi un file:

`bzip2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Decomprimi un file:

`bzip2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_compresso.bz2</span>

- Decomprimi un file e mostrane il contenuto su standard output:

`bzip2 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_compresso.bz2</span>
