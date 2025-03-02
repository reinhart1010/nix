---
layout: page
title: common/egrep (Indonesia)
description: "Cari pola teks tertentu pada kumpulan berkas menggunakan kata pencarian ekspresi reguler (regex) tingkat lanjut (mendukung `?`, `+`, `{}`, `()`, dan `|`)."
content_hash: 43f6ea1c75fce1cab86d0753fcef0f27dddb52fb
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/egrep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/egrep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/egrep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/egrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# egrep

Cari pola teks tertentu pada kumpulan berkas menggunakan kata pencarian ekspresi reguler (regex) tingkat lanjut (mendukung `?`, `+`, `{}`, `()`, dan `|`).
Informasi lebih lanjut: <https://manned.org/egrep>.

- Cari suatu berkas untuk teks yang mengikuti pola pencarian tertentu:

`egrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Cari lebih dari satu berkas untuk teks yang mengikuti pola pencarian tertentu:

`egrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Cari isi `stdin` untuk teks yang mengikuti pola pencarian tertentu:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` | egrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>

- Cetak nama berkas dan nomor baris di mana pola tersebut ditemukan:

`egrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Cari seluruh berkas selain berkas format biner di dalam suatu direktori secara rekursif (termasuk berkas-berkas di dalam subdirektori) dengan menunjukkan nomor barisan di mana pola tersebut ditemukan:

`egrep --recursive --binary-files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">without-match</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Cari untuk barisan teks yang tidak memenuhi kriteria pada pola pencarian:

`egrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>
