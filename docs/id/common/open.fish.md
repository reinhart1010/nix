---
layout: page
title: common/open.fish (Indonesia)
description: "Buka file, direktori, dan alamat URI dengan aplikasi-aplikasi default yang dapat membukanya."
content_hash: 2f46db26a5f5e14607f29fe39011cbe2c5e6808a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/open.fish.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/open.fish.html
    icon: bi bi-globe
tldri18n_status: 2
---
# open

Buka file, direktori, dan alamat URI dengan aplikasi-aplikasi default yang dapat membukanya.
Perintah ini tersedia melalui `fish` dalam sistem operasi yang tidak menawarkan perintah `open` secara bawaan (seperti Haiku dan macOS).
Informasi lebih lanjut: <https://fishshell.com/docs/current/cmds/open.html>.

- Buka sebuah file di dalam aplikasi default:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Buka semua file dengan ekstensi tertentu di dalam aplikasi default pada direktori saat ini:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>

- Buka sebuah direktori di dalam aplikasi manajer file default:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Buka sebuah situs web di dalam aplikasi peramban default:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Buka sebuah alamat URI di dalam aplikasi default yang dapat menanganinya:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>
