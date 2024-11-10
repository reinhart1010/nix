---
layout: page
title: common/hsw-cli (Indonesia)
description: "Alat baris perintah untuk mengakses dompet digital Handshake melalui koneksi REST API."
content_hash: 7254edd5c11295afd8520d6ece85a7064785216a
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/hsw-cli.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/hsw-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hsw-cli

Alat baris perintah untuk mengakses dompet digital Handshake melalui koneksi REST API.
Informasi lebih lanjut: <https://github.com/handshake-org/hs-client>.

- Buka akses terhadap suatu dompet digital (nilai timeout dalam hitungan detik):

`hsw-cli unlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timeout</span>

- Kunci dompet saat ini:

`hsw-cli lock`

- Tampilkan informasi terhadap dompet saat ini:

`hsw-cli get`

- Tampilkan saldo dompet saat ini:

`hsw-cli balance`

- Tampilkan riwayat transaksi yang menggunakan dompet saat ini:

`hsw-cli history`

- Kirim suatu transaksi dengan suatu nominal koin menuju suatu alamat dompet tujuan:

`hsw-cli send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_tujuan</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.05</span>

- Tampilkan daftar transaksi yang berstatus tertunda (pending) yang melibatkan dompet ini:

`hsw-cli pending`

- Tampilkan informasi rincian suatu transaksi:

`hsw-cli tx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_transaksi</span>
