---
layout: page
title: sunos/prstat (Indonesia)
description: "Laporkan statistik proses aktif."
content_hash: 6a06a7ad19a465f6888a8813af096cf6f71878f7
last_modified_at: 2024-04-10
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prstat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prstat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prstat

Laporkan statistik proses aktif.
Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Periksa semua proses dan laporan statistik yang diurutkan berdasarkan tingkat penggunaan CPU:

`prstat`

- Periksa semua proses dan laporan statistik yang disortir berdasarkan penggunaan memori:

`prstat -s rss`

- Laporkan ringkasan total penggunaan untuk tiap user:

`prstat -t`

- Laporkan informasi pengukuran proses microstate:

`prstat -m`

- Cetak daftar penggunaan CPU 5 proses teratas tiap 1 detik:

`prstat -c -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -s cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
