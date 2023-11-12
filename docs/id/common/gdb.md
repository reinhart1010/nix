---
layout: page
title: common/gdb (Indonesia)
description: "GNU Debugger."
content_hash: b7d08ca5b9fb29da37fae3b70cbdfa7829ed5427
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/gdb.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gdb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gdb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gdb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gdb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdb

GNU Debugger.
Informasi lebih lanjut: <https://www.gnu.org/software/gdb>.

- Menjalankan debug pada sebuah berkas yang dapat dieksekusi:

`gdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_exe</span>

- Menambahkan sebuah proses pada gdb:

`gdb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_exe</span>

- Menjalankan debug dengan berkas core:

`gdb -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">core</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_exe</span>

- Mengeksekusi perintah GDB pada saat dijanlakan:

`gdb -ex "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_exe</span>

- Menjalankan gdb dan melemparkan argumen pada berkas yang dieksekusi:

`gdb --args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_exe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumen1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumen2</span>
