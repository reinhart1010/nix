---
layout: page
title: common/accelerate (Indonesia)
description: "Sebuah pustaka/library yang memungkinkan kode PyTorch yang sama dapat dijalankan secara menyebar."
content_hash: 4c2e710b9ed2d7065f18ed9cb60866f3958afc03
last_modified_at: 2023-12-31
related_topics:
  - title: English version
    url: /en/common/accelerate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/accelerate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/accelerate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Accelerate

Sebuah pustaka/library yang memungkinkan kode PyTorch yang sama dapat dijalankan secara menyebar.
Informasi lebih lanjut: <https://huggingface.co/docs/accelerate/index>.

- Tampilkan informasi lingkungan proyek PyTorch saat ini:

`accelerate env`

- Buat file konfigurasi secara interaktif:

`accelerate config`

- Tampilkan prakiraan kapasitas memori GPU yang dibutuhkan untuk menjalankan model Hugging Face dengan tipe data yang berbeda:

`accelerate estimate-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama/model</span>

- Uji validitas sebuah file konfigurasi Accelerate:

`accelerate test --config_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/config.yaml</span>

- Jalankan sebuah model PyTorch dengan Accelerate, menggunakan CPU saja:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/script.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--cpu</span>

- Jalankan model dengan Accelerate, menggunakan GPU dari 2 perangkat yang berbeda:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/script.py</span>` --multi_gpu --num_machines 2`
