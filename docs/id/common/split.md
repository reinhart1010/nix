---
layout: page
title: common/split (Indonesia)
description: "Memisahkan sebuah file menjadi beberapa bagian."
content_hash: fd5b0a5c0e324085db7ee0fdb069453456fb2d1a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/split.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/split.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/split.html
    icon: bi bi-globe
tldri18n_status: 2
---
# split

Memisahkan sebuah file menjadi beberapa bagian.
Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html>.

- Memisahkan sebuah file, tiap bagian memiliki 10 baris (kecuali di bagian terakhir):

`split -l 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Memisahkan sebuah file menjadi 5 file. Dibagi sehingga masing-masing bagian memiliki ukuran yang sama (kecuali di bagian terakhir):

`split -n 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Memisahkan sebuah file dengan ukuran 512 byte masing-masing bagiannya (kecuali di bagian terakhir; gunakan 512k untuk kilobyte dan 512m untuk megabytes):

`split -b 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Memisahkan sebuah file dengan ukuran paling banyak 512 byte masing-masing bagiannya tanpa memotong baris:

`split -C 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>
