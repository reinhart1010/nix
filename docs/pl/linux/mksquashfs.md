---
layout: page
title: linux/mksquashfs (polski)
description: "Utwórz lub dodaj pliki i katalogi do systemów plików squashfs."
content_hash: 15772c765407b455c133a5bef24ba7eba3b011ba
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/mksquashfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mksquashfs

Utwórz lub dodaj pliki i katalogi do systemów plików squashfs.
Więcej informacji: <https://manned.org/mksquashfs>.

- Utwórz lub dodaj pliki i katalogi do systemu plików squashfs (domyślnie kompresując za pomocą `gzip`):

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu1 ścieżka/do/pliku_lub_katalogu2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>

- Utwórz lub dodaj pliki i katalogi do systemu plików squashfs, używając podanego algorytmu kompresji ([comp]ression):

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu1 ścieżka/do/pliku_lub_katalogu2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>` -comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gzip|lzo|lz4|xz|zstd|lzma</span>

- Utwórz lub dodaj pliki i katalogi do systemu plików squashfs, pomijając ([e]xcluding) niektóre z nich:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu1 ścieżka/do/pliku_lub_katalogu2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik|katalog1 plik|katalog2 ...</span>

- Utwórz lub dodaj pliki i katalogi do systemu plików squashfs, pomijając ([e]xcluding) te kończące się na `.gz`:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu1 ścieżka/do/pliku_lub_katalogu2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>` -wildcards -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.gz</span>`"`

- Utwórz lub dodaj pliki i katalogi do systemu plików squashfs, pomijając ([e]xcluding) te pasujące do wyrażenia regularnego:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu1 ścieżka/do/pliku_lub_katalogu2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>` -regex -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wyrażenie_regularne</span>`"`
