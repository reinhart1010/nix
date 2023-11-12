---
layout: page
title: common/rails-generate (Indonesia)
description: "Membuat Rails templates yang baru ke suatu proyek."
content_hash: 5d6ab70b53f2badcacffd5976d711f297a97ebf0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/rails-generate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rails-generate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rails generate

Membuat Rails templates yang baru ke suatu proyek.
Informasi lebih lanjut: <https://guides.rubyonrails.org/command_line.html#bin-rails-generate>.

- Menampilkan semua generator yang tersedia:

`rails generate`

- Membuat model baru bernama Post dengan atribut judul dan uraian:

`rails generate model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">judul:string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uraian:text</span>

- Mmebuat _controller_ baru bernama Posts dengan actions index, show, new dan create:

`rails generate controller `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Posts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">create</span>

- Membuat migrasi baru yang menambahkan atribut kategori ke model yang sudah ada bernama Post:

`rails generate migration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AddKategoriToPost</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kategori:string</span>

- Membuat _scaffold_ untuk model bernama Post, dengan pendefinisian atribut judul dan uraian:

`rails generate scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title:string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">body:text</span>
