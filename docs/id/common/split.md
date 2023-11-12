---
layout: page
title: common/split (Indonesia)
description: "Memisahkan sebuah file menjadi beberapa bagian."
content_hash: 26f854e86843f7c6c57d74dcf76507379e3d1cd6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/split.html
    icon: bi bi-globe
tldri18n_status: 2
---
# split

Memisahkan sebuah file menjadi beberapa bagian.
Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/split>.

- Memisahkan sebuah file, tiap bagian memiliki 10 baris (kecuali di bagian terakhir):

`split -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>

- Memisahkan sebuah file menjadi 5 file. Dibagi sehingga masing-masing bagian memiliki ukuran yang sama (kecuali di bagian terakhir):

`split -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>

- Memisahkan sebuah file dengan ukuran 512 byte masing-masing bagiannya (kecuali di bagian terakhir; gunakan 512k untuk kilobyte dan 512m untuk megabytes):

`split -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>

- Memisahkan sebuah file dengan ukuran paling banyak 512 byte masing-masing bagiannya tanpa memotong baris:

`split -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>
