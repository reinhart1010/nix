---
layout: page
title: common/rails-routes (Indonesia)
description: "Menampilkan daftar _routes_ di aplikasi Rails."
content_hash: 2314b744ba8221530bf4631080d6d6edbae7e1d9
related_topics:
  - title: English version
    url: /en/common/rails-routes.html
    icon: bi bi-globe
---
# rails routes

Menampilkan daftar _routes_ di aplikasi Rails.
Informasi lebih lanjut: <https://guides.rubyonrails.org/routing.html>.

- Menampilkan semua _routes_:

`rails routes`

- Menampilkan semua _routes_ dengan format yang lebih panjang:

`rails routes --expanded`

- Menampilkan _routes_ yang sebagian cocok dengan nama helper method URL, HTTP verb, atau path URL:

`rails routes -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posts_path|GET|/posts</span>

- Menampilkan _routes_ yang memetakan ke controller tertentu:

`rails routes -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posts|Posts|Blogs::PostsController</span>
