---
layout: page
title: common/rspec (Indonesia)
description: "Kerangka pengujian dalam Behavior-driven development yang ditulis dalam bahasa Ruby untuk menguji kode Ruby."
content_hash: f8949488bc3db6e6867a1e11701052628e3e4a71
last_modified_at: 2024-02-01
related_topics:
  - title: English version
    url: /en/common/rspec.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rspec

Kerangka pengujian dalam Behavior-driven development yang ditulis dalam bahasa Ruby untuk menguji kode Ruby.
Informasi lebih lanjut: <https://rspec.info>.

- Menginisiasi file konfigurasi `.rspec` dan spec helper:

`rspec --init`

- Menjalankan semua file tes:

`rspec`

- Menjalankan file tes dalam direktori khusus:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/directory</span>

- Menjalankan file tes khusus:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Menjalankan beberapa file tes:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file2</span>

- Menjalankan kasus khusus dalam file tes (misalnya tes yang ada di baris 83):

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">83</span>

- Menjalankan tes dengan seed khusus:

`rspec --seed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">angka_seed</span>
