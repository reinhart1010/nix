---
layout: page
title: common/rubocop (Indonesia)
description: "Analisa berkas Ruby."
content_hash: 153b97d4f75825a00ad4c5c6f8365a7088d5e4d9
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/common/rubocop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rubocop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/rubocop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rubocop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rubocop

Analisa berkas Ruby.
Informasi lebih lanjut: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Periksa semua berkas dalam direktori saat ini (termasuk direktori-direktori di dalamnya):

`rubocop`

- Periksa satu atau lebih berkas atau direktori secara khusus:

`rubocop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...</span>

- Tulis output ke berkas:

`rubocop --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Lihat daftar cop (aturan-aturan dalam menganalisa):

`rubocop --show-cops`

- Kecualikan kumpulan cop dalam proses analisa:

`rubocop --except `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop1 cop2 ...</span>

- Jalankan hanya beberapa cop:

`rubocop --only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop1 cop2 ...</span>

- Perbaiki berkas secara otomatis (fitur percobaan):

`rubocop --auto-correct`
