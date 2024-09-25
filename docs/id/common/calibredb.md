---
layout: page
title: common/calibredb (Indonesia)
description: "Kelola suatu pangkalan data perpustakaan buku digital."
content_hash: f4abc7d854b198ec0c9295d233712a4f66a87c2c
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/calibredb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/calibredb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/calibredb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calibredb

Kelola suatu pangkalan data perpustakaan buku digital.
Bagian dari aplikasi perpustakaan buku digital Calibre.
Informasi lebih lanjut: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- Tampilkan daftar judul dan informasi tambahan terkait buku-buku digital yang telah terdaftar dalam perpustakaan:

`calibredb list`

- Cari kumpulan buku dengan informasi tambahan:

`calibredb list --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>

- Hanya tampilkan nomor induk (id) dari hasil pustaka pencarian:

`calibredb search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>

- Masukkan satu atau beberapa buku baru ke dalam perpustakaan:

`calibredb add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Masukkan seluruh buku dalam suatu direktori secara [r]ekursif:

`calibredb add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recurse</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Hapus satu atau beberapa buku dari perpustakaan. Anda perlu memasukkan nomor-nomor induk (lihat keterangan di atas):

`calibredb remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id1 id2 ...</span>
