---
layout: page
title: sunos/svcs (Indonesia)
description: "Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan."
content_hash: 4d46e9dadfafa24071291358ceb6dac15fdc6e66
last_modified_at: 2024-04-10
related_topics:
  - title: English version
    url: /en/sunos/svcs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcs.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svcs

Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan.
Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1/svcs>.

- Daftar semua servis yang berjalan:

`svcs`

- Daftar servis-servis yang tidak berjalan:

`svcs -vx`

- Daftar informasi tentang sebuah servis:

`svcs apache`

- Tampilkan lokasi dari berkas catatan servis:

`svcs -L apache`

- Display end of a service log file:

`tail $(svcs -L apache)`
