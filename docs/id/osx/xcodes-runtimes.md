---
layout: page
title: osx/xcodes-runtimes (Indonesia)
description: "Atur pemasangan runtime Simulator yang tersedia bagi aplikasi Xcode."
content_hash: c5954a6ca3ba55c6992111c993693e580b59b212
last_modified_at: 2023-10-30
related_topics:
  - title: English version
    url: /en/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/xcodes-runtimes.html
    icon: bi bi-globe
---
# xcodes runtimes

Atur pemasangan runtime Simulator yang tersedia bagi aplikasi Xcode.
Informasi lebih lanjut: <https://github.com/xcodesorg/xcodes>.

- Tampilkan seluruh Simulator yang tersedia bagi aplikasi Xcode:

`xcodes runtimes --include-betas`

- Unduh sebuah runtime Simulator:

`xcodes runtimes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_runtime</span>

- Unduh dan pasang sebuah runtime Simulator:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_runtime</span>

- Unduh/pasang runtime Simulator untuk iOS/watchOS/tvOS/visionOS versi spesifik (nama harus ditulis sebagai case-sensitive):

`xcodes runtimes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">download|install</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iOS|watchOS|tvOS|visionOS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_runtime</span>`"`

- Atur lokasi penyimpanan arsip runtime yang akan diunduh (nilai default: `~/Downloads`):

`xcodes runtimes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">download|install</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_runtime</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Jangan hapus arsip runtime Simulator setelah pemasangan selesai:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_runtime</span>` --keep-archive`
