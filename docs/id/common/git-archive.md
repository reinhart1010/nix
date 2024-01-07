---
layout: page
title: common/git-archive (Indonesia)
description: "Buat sebuah arsip direktori berdasarkan cabang/tree tertentu."
content_hash: bfe5ca1caa90c170c2ed579b196afbb9a01f28de
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/common/git-archive.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-archive.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-archive.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-archive.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-archive.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-archive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git archive

Buat sebuah arsip direktori berdasarkan cabang/tree tertentu.
Informasi lebih lanjut: <https://git-scm.com/docs/git-archive>.

- Buat sebuah arsip tar berisikan isi dari tree HEAD saat ini, kemudian tampilkan isi file arsip mentah menuju `stdout`:

`git archive --verbose HEAD`

- Buat sebuah arsip zip dari tree HEAD saat ini, kemudian tampilkan isi file arsip mentah menuju `stdout`:

`git archive --verbose --format zip HEAD`

- Lakukan hal yang sama, namun simpan arsip zip ke dalam suatu direktori:

`git archive --verbose --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.zip</span>` HEAD`

- Buat arsip tar dari komit terakhir pada cabang tertentu:

`git archive --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Buat arsip tar berdasaran subdirektori tertentu pada suatu repositori Git:

`git archive --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.tar</span>` HEAD:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Bubuhkan nama jalur pada awal nama setiap file, untuk diarsipkan di dalam direktori tertentu:

`git archive --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.tar</span>` --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/untuk/dibubuhkan</span>`/ HEAD`
