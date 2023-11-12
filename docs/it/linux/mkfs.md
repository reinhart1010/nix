---
layout: page
title: linux/mkfs (italiano)
description: "Costruisce un filesystem Linux su una partizione del disco rigido."
content_hash: 5b4cbb8356b8593866cfa03404f93492e3241035
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/mkfs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/mkfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs

Costruisce un filesystem Linux su una partizione del disco rigido.
Questo comando è deprecato in favore degli strumenti specifici per filesystem: mkfs.tipo.
Maggiori informazioni: <https://manned.org/mkfs>.

- Costruisce un filesystem Linux ext2 su una partizione:

`mkfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/partizione</span>

- Costruisce un filesystem del tipo specificato:

`mkfs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/partizione</span>

- Costruisce un filesystem del specificato e controlla la presenza di settori danneggiati:

`mkfs -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/partizione</span>
