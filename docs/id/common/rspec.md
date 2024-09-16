---
layout: page
title: common/rspec (Indonesia)
description: "Kerangka pengujian kode Ruby berbasis Ruby dan pola pengembangan berbasis kebiasaan (behavior-driven development)."
content_hash: d07dc079a94d0bfc6e63451356adeab48e80c410
last_modified_at: 2024-09-16
related_topics:
  - title: English version
    url: /en/common/rspec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rspec

Kerangka pengujian kode Ruby berbasis Ruby dan pola pengembangan berbasis kebiasaan (behavior-driven development).
Informasi lebih lanjut: <https://rspec.info>.

- Buat suatu berkas konfigurasi `.rspec` dan berkas pendukung spesifikasi pengujian (spec helper):

`rspec --init`

- Jalankan semua pengujian menurut berkas-berkas spesifikasi:

`rspec`

- Jalankan pengujian menurut berkas-berkas spesifikasi dalam direktori khusus:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Jalankan beberapa pengujian menurut kumpulan berkas spesifikasi:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Jalankan kasus khusus dalam pengujian menurut berkas-berkas spesifikasi (misalnya tes yang ada di baris 83):

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">83</span>

- Jalankan tes dengan seed khusus (untuk pengujian berbasis randomisasi):

`rspec --seed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">angka_seed</span>
