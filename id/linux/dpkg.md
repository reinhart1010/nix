---
layout: page
title: linux/dpkg (Indonesia)
description: "Manajer paket Debian."
content_hash: e5b29f66eba8290cd0958ad81ae1a82673b616e2
related_topics:
  - title: Deutsch version
    url: /de/linux/dpkg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dpkg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dpkg

Manajer paket Debian.
Beberapa subperintah seperti `dpkg deb` memiliki dokumentasi penggunaannya sendiri.
Informasi lebih lanjut: <https://manpages.debian.org/buster/dpkg/dpkg.1.en.html>.

- Memasang paket dari sebuah file DEB:

`dpkg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.deb</span>

- Menghapus pemasangan sebuah paket:

`dpkg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Memperlihatkan daftar paket terinstal:

`dpkg -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola</span>

- Memperlihatkan isi sebuah paket:

`dpkg -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Memperlihatkan isi sebuah paket lokal:

`dpkg -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.deb</span>

- Mencari tahu paket yang memiliki sebuah file:

`dpkg -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>
