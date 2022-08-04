---
layout: page
title: linux/mkfs (italiano)
description: "Costruisce un filesystem Linux su una partizione del disco rigido."
content_hash: 988de8055791df99cdc56b9146df55809bb9c72b
related_topics:
  - title: English version
    url: /en/linux/mkfs.html
    icon: bi bi-globe
---
# mkfs

Costruisce un filesystem Linux su una partizione del disco rigido.
Questo comando è deprecato in favore degli strumenti specifici per filesystem: mkfs.tipo.
Maggiori informazioni: <https://manned.org/mkfs>.

- Costruisce un filesystem Linux ext2 su una partizione:

`mkfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/partizione</span>

- Costruisce un filesystem del tipo specificato:

`mkfs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/partizione</span>

- Costruisce un filesystem del specificato e controlla la presenza di settori danneggiati:

`mkfs -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/partizione</span>
