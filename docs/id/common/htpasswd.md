---
layout: page
title: common/htpasswd (Indonesia)
description: "Buat dan atur isi berkas-berkas htpasswd untuk melindungi kumpulan direktori yang diakses oleh peladen web menggunakan metode autentikasi sederhana/basic."
content_hash: ea7a0f1bb80d2c3477f51130865cb896ff3e698c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/htpasswd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/htpasswd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# htpasswd

Buat dan atur isi berkas-berkas htpasswd untuk melindungi kumpulan direktori yang diakses oleh peladen web menggunakan metode autentikasi sederhana/basic.
Informasi lebih lanjut: <https://httpd.apache.org/docs/current/programs/htpasswd.html>.

- Buat/timpa isi berkas htpasswd:

`htpasswd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Tambahkan atau mutakhirkan konfigurasi bagi suatu akun pengguna (dalam mengakses layanan web) ke dalam berkas htpasswd:

`htpasswd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Tambahkan suatu akun pengguna kepada berkas htpasswd dalam mode batch, dengan melewati proses pemasukkan kata sandi secara interaktif (untuk penggunaan dalam skrip syel):

`htpasswd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>

- Hapus konfigurasi akses suatu akun pengguna dari isi suatu berkas htpasswd:

`htpasswd -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Lakukan proses verifikasi kata sandi bagi suatu akun pengguna:

`htpasswd -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Tampilkan suatu string berisikan username (akun pengguna, dalam plain text) dan kata sandi (dalam hash md5):

`htpasswd -nbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>
