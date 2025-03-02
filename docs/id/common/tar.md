---
layout: page
title: common/tar (Indonesia)
description: "Alat pengarsip berkas."
content_hash: 965fc2e2f9cdf04374d344be22101b64ba4bf8b1
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/common/tar.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/tar.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tar.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tar.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tar.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tar.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tar.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tar.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/tar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tar

Alat pengarsip berkas.
Sering digunakan bersamaan dengan alat kompresi tertentu, seperti `gzip` atau `bzip2`.
Informasi lebih lanjut: <https://www.gnu.org/software/tar>.

- Buat ([c]reate) suatu arsip dan simpan ke dalam suatu berkas ([f]ile):

`tar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/target.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Buat ([c]reate) suatu arsip dengan tambahan kompresi g[z]ip dan simpan ke dalam suatu berkas ([f]ile):

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/target.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Buat ([c]reate) suatu arsip dengan tambahan kompresi g[z]ip dari suatu direktori mengunakan alamat berkas relatif:

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/target.tar.gz</span>` --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>` .`

- E[x]trak suatu berkas ([f]ile) arsip (biasa atau terkompres) menuju direktori saat ini dengan menampilkan rincian operasi (mode [v]erbose):

`tar xvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber.tar[.gz|.bz2|.xz]</span>

- E[x]trak suatu berkas ([f]ile) arsip (biasa atau terkompres) menuju direktori target yang ditentukan:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber.tar[.gz|.bz2|.xz]</span>` --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Buat ([c]reate) suatu arsip  terkompres dan simpan di dalam suatu berkas ([f]ile), menggunakan metode kompresi yang ditentukan secara otom[a]tis berdasarkan nama ekstensi berkas tujuan:

`tar caf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/target.tar.xz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- [t]ampilkan isi suatu berkas ([f]ile) tar secara rinci (mode [v]erbose):

`tar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber.tar</span>

- E[x]trak kumpulan berkas yang namanya memenuhi pola kriteria yang ditentukan dari suatu berkas ([f]ile) arsip:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber.tar</span>` --wildcards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.html</span>`"`
