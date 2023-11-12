---
layout: page
title: linux/sqfstar (polski)
description: "Utwórz system plików squashfs z archiwum tar."
content_hash: 361a6e6afd7543b41a70836448815945403bf821
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/sqfstar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sqfstar

Utwórz system plików squashfs z archiwum tar.
Więcej informacji: <https://manned.org/sqfstar>.

- Utwórz system plików squashfs (domyślnie kompresując za pomocą `gzip`) z nieskompresowanego archiwum tar:

`sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archiwum.tar</span>

- Utwórz system plików squashfs z archiwum tar skompresowanego za pomocą `gzip`, i skompresuj system plików używając podanego algorytmu:

`zcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archiwum.tar.gz</span>` | sqfstar -comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gzip|lzo|lz4|xz|zstd|lzma</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>

- Utwórz system plików squashfs z archiwum tar skompresowanego za pomocą `xz`, pomijając niektóre pliki:

`xzcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archiwum.tar.xz</span>` | sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik1 plik2 ...</span>

- Utwórz system plików squashfs z archiwum tar skompresowanego za pomocą `zstd`, pomijając pliki kończące się na `.gz`:

`zstdcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archiwum.tar.zst</span>` | sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.gz</span>`"`

- Utwórz system plików squashfs z archiwum tar skompresowanego za pomocą `lz4`, pomijając pliki pasujące do wyrażenia regularnego:

`lz4cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archiwum.tar.lz4</span>` | sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>` -regex "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wyrażenie_regularne</span>`"`
