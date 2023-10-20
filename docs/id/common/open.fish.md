---
layout: page
title: common/open.fish (Indonesia)
description: "Buka file, direktori, dan alamat URI dengan aplikasi-aplikasi default yang dapat membukanya."
content_hash: 9d3a148d306316f084dadf9dcfa9fe101a69bc8f
last_modified_at: 2023-10-20
related_topics:
  - title: English version
    url: /en/common/open.fish.html
    icon: bi bi-globe
---
# open

Buka file, direktori, dan alamat URI dengan aplikasi-aplikasi default yang dapat membukanya.
Perintah ini tersedia melalui `fish` dalam sistem operasi yang tidak menawarkan perintah `open` secara bawaan (seperti Haiku dan macOS).
Informasi lebih lanjut: <https://fishshell.com/docs/current/cmds/open.html>

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
