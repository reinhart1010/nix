---
layout: page
title: linux/dpkg (Indonesia)
description: "Manajer paket Debian."
content_hash: 3b767a004df34a3c1690b7847c198d12434d9d39
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/linux/dpkg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dpkg.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/dpkg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dpkg

Manajer paket Debian.
Beberapa subperintah seperti `dpkg deb` memiliki dokumentasi penggunaannya sendiri.
Informasi lebih lanjut: <https://manned.org/dpkg>.

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
