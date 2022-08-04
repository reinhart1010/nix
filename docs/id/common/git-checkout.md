---
layout: page
title: common/git-checkout (Indonesia)
description: "Checkout cabang atau alamat ke direktori kerja."
content_hash: 9066c5e22fddf9f2f3b277a5cb52578ba3c9a40e
related_topics:
  - title: English version
    url: /en/common/git-checkout.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-checkout.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-checkout.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-checkout.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-checkout.html
    icon: bi bi-globe
---
# git checkout

Checkout cabang atau alamat ke direktori kerja.
Informasi lebih lanjut: <https://git-scm.com/docs/git-checkout>.

- Membuat dan beralih ke cabang baru:

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Membuat dan beralih ke cabang baru berdasarkan referensi tertentu (misal cabang, remote, cabang remote, dan tag):

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">referense</span>

- Beralih ke cabang lokal yang ada:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Beralih ke cabang yang sebelumnya di checkout:

`git checkout -`

- Beralih ke cabang remote yang ada:

`git checkout --track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Menyingkirkan semua perubahan yang tidak masuk status stage pada direktori saat ini (lihat `git reset` untuk perintah yang lebih mirip undo):

`git checkout .`

- Menyingkirkan perubahan yang tidak masuk status stage pada berkas:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas</span>

- Mengganti berkas pada direktori saat ini dengan versi pada cabang lain:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas</span>
