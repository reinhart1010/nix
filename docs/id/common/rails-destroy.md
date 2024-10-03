---
layout: page
title: common/rails-destroy (Indonesia)
description: "Menghapus sumber daya (resources) yang dikelola dalam suatu proyek Rails."
content_hash: 3a21fb9c7aeff688b16a6d1e66432779a84e958c
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/rails-destroy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rails destroy

Menghapus sumber daya (resources) yang dikelola dalam suatu proyek Rails.
Informasi lebih lanjut: <https://guides.rubyonrails.org/command_line.html#bin-rails-destroy>.

- Tampilkan daftar semua generator yang tersedia untuk membantu proses penghapusan:

`rails destroy`

- Hapus suatu model yang bernama Post:

`rails destroy model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Post</span>

- Hapus suatu controller yang bernama Posts:

`rails destroy controller `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Posts</span>

- Hapus suatu migrasi yang membuat Posts:

`rails destroy migration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CreatePosts</span>

- Hapus suatu scaffold bagi model Post:

`rails destroy scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Post</span>
