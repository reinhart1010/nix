---
layout: page
title: common/git-bisect (Indonesia)
description: "Lakukan strategi pencarian/pembelahan biner untuk mencari komit yang menyebabkan masalah/bug."
content_hash: 8bdb7d70e17658dc782c7b175b3ec7e9707a5626
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/common/git-bisect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-bisect.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bisect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bisect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bisect.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bisect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bisect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bisect

Lakukan strategi pencarian/pembelahan biner untuk mencari komit yang menyebabkan masalah/bug.
Git akan secara otomatis melompat bolak-balik dalam grafik komit untuk semakin mempersempit kandidat komit yang bermasalah.
Informasi lebih lanjut: <https://git-scm.com/docs/git-bisect>.

- Jalankan sesi pembelahan biner pada suatu rentang komit antara komit bermasalah dan komit (biasanya terdahulu) yang diketahui tak bermasalah:

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komit_bermasalah</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komit_baik</span>

- Untuk setiap komit yang dipilih oleh `git bisect`, tandai komit tersebut sebagai baik (good) atau buruk (bad) setelah mencobanya:

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good|bad</span>

- Setelah `git bisect` berhasil menemukan komit yang bermasalah, akhiri sesi pembelahan dan kembali kepada cabang sebelumnya:

`git bisect reset`

- Lewati pengecekan suatu komit saat proses pembelahan berlangsung (misal: karena terdapat masalah yang disebabkan oleh faktor lain):

`git bisect skip`

- Tampilkan log tentang kemajuan proses pembelahan saat ini:

`git bisect log`
