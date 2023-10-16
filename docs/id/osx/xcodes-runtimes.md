---
layout: page
title: osx/xcodes-runtimes (Indonesia)
description: "Atur pemasangan runtime Simulator yang tersedia bagi aplikasi Xcode."
content_hash: f5574e382fa55ce7b2b91ea9e323b015923e29a7
last_modified_at: 2023-10-16
related_topics:
  - title: English version
    url: /en/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/xcodes-runtimes.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xcodes runtimes

Atur pemasangan runtime Simulator yang tersedia bagi aplikasi Xcode.
Informasi lebih lanjut: <https://github.com/xcodesorg/xcodes>.

- Tampilkan seluruh Simulator yang tersedia bagi aplikasi Xcode:

`xcodes runtimes --include-betas`

- Unduh sebuah runtime Simulator:

`xcodes runtimes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_runtime</span>

- Unduh dan pasang sebuah runtime Simulator:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_runtime</span>
