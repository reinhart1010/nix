---
layout: page
title: common/composer (Indonesia)
description: "Manajer paket untuk proyek PHP."
content_hash: d61fc1f503a5c06ce4c55b066da794799bebcf9c
related_topics:
  - title: English version
    url: /en/common/composer.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/composer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/composer.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># composer

Manajer paket untuk proyek PHP.
Informasi lebih lanjut: <https://getcomposer.org/>.

- Membuat file `composer.json` secara interaktif:

`composer init`

- Menambahkan paket sebagai dependensi untuk proyek ini, menambahkan ke `composer.json`:

`composer require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/nama_paket</span>

- Menginstal semua dependensi dalam `composer.json` proyek ini dan membuat `composer.lock`:

`composer install`

- Menghapus sebuah paket dari proyek ini, menghapus paket tersebut sebagai ketergantungan dari `composer.json`:

`composer remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/nama_paket</span>

- Memperbarui semua dependensi dalam `composer.json` proyek ini dan memperbarui versi di file `composer.lock`:

`composer update`

- Memperbarui `composer.lock` setelah mengubah `composer.json` secara manual:

`composer update --lock`

- Memcari tahu mengapa sebuah dependensi tidak dapat diinstal:

`composer why-not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/nama_paket</span>

- Memperbarui composer ke versi terbaru:

`composer self-update`
