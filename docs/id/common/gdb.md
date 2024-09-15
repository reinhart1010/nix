---
layout: page
title: common/gdb (Indonesia)
description: "GNU Debugger, alat pengawakutu program komputer."
content_hash: 24a6e03e1871458a1b71d560042ae6a82b9bb274
last_modified_at: 2024-09-15
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

GNU Debugger, alat pengawakutu program komputer.
Informasi lebih lanjut: <https://www.gnu.org/software/gdb>.

- Jalankan pengawakutu pada sebuah berkas program yang dapat dieksekusi:

`gdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_exe</span>

- Tambahkan suatu proses untuk diawasi oleh gdb:

`gdb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_exe</span>

- Jalankan pengawakutu dengan berkas core:

`gdb -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">core</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_exe</span>

- Kirim perintah menuju pengawakutu pada saat dijalankan:

`gdb -ex "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_exe</span>

- Lemparkan argumen terhadap berkas program yang dieksekusi saat hendak diawasi oleh GDB:

`gdb --args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_exe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumen1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumen2</span>
