---
layout: page
title: sunos/prstat (Indonesia)
description: "Laporkan statistik proses aktif."
content_hash: b57d202a2ce71f50278a43f08f0bb0c03be5fb17
last_modified_at: 2024-06-19
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
  - title: polski version
    url: /pl/sunos/prstat.html
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

`prstat -c -n 5 -s cpu 1`
