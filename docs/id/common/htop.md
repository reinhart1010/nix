---
layout: page
title: common/htop (Indonesia)
description: "Tampilkan informasi waktu nyata dinamis tentang proses yang berjalan. Versi `top` yang disempurnakan."
content_hash: 0fa98ab9e87f6668b73c85b2f780f8c28416d12f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/htop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/htop.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/htop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/htop.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/htop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/htop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/htop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# htop

Tampilkan informasi waktu nyata dinamis tentang proses yang berjalan. Versi `top` yang disempurnakan.
Informasi lebih lanjut: <https://htop.dev/>.

- Mulai `htop`:

`htop`

- Mulai `htop` dan tampilkan proses yang dimiliki oleh pengguna tertentu:

`htop --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Tampilkan daftar proses beserta hierarki penugasannya dalam bentuk tampilan pohon untuk menunjukkan relasi proses induk beserta anak-anaknya:

`htop --tree`

- Urutkan proses berdasarkan `sort_item` yang ditentukan (gunakan `htop --sort help` untuk opsi yang tersedia  ):

`htop --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sort_item</span>

- Jalankan `htop` dengan jangka waktu pemuatan ulang (refresh) data tertentu, dalam bentuk sepersepuluh detik (yakni 50 = 5 detik):

`htop --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- Lihat perintah interaktif saat menjalankan htop:

`?`

- Alihkan tampilan menuju tab lain:

`tab`

- Tampilkan bantuan:

`htop --help`
