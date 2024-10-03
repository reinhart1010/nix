---
layout: page
title: common/composer (Indonesia)
description: "Manajer paket untuk proyek PHP."
content_hash: 052dad431e7e86fd383296db5c344c44d022fab3
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/composer.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/composer.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/composer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/composer.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/composer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# composer

Manajer paket untuk proyek PHP.
Informasi lebih lanjut: <https://getcomposer.org/>.

- Buat sebuah berkas `composer.json` secara interaktif:

`composer init`

- Tambahkan paket sebagai sebuah pustaka prasyarat (dependency) untuk proyek ini, menambahkan ke `composer.json`:

`composer require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna/nama_paket</span>

- Pasang seluruh prasyarat dalam `composer.json` proyek ini dan buat berkas `composer.lock`:

`composer install`

- Hapus pemasangan suatu paket dalam proyek ini, sehingga menghapusnya dari entri prasyarat pada `composer.json` dan `composer.lock`:

`composer remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna/nama_paket</span>

- Perbarui semua pustaka prasyarat dalam `composer.json` proyek ini dan catat versi-versi terkini dalam berkas `composer.lock`:

`composer update`

- Memperbarui `composer.lock` setelah mengubah `composer.json` secara manual:

`composer update --lock`

- Cari tahu alasa mengapa sebuah dependensi tidak dapat dipasang:

`composer why-not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/nama_paket</span>

- Perbarui program composer menuju versi terbaru:

`composer self-update`
