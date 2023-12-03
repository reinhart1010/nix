---
layout: page
title: osx/goku (Indonesia)
description: "Atur konfigurasi Karabiner."
content_hash: a2ce2cccddf62abf5f5001c1cd2e00fd9d80bf14
last_modified_at: 2023-12-03
related_topics:
  - title: English version
    url: /en/osx/goku.html
    icon: bi bi-globe
tldri18n_status: 2
---
# goku

Atur konfigurasi Karabiner.
Informasi lebih lanjut: <https://github.com/yqrashawn/GokuRakuJoudo>.

- Buat file `karabiner.json` dengan konfigurasi default:

`goku`

- Buat file `karabiner.json` menggunakan konfigurasi khusus dari `config.edn`:

`goku --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/config.edn</span>

- Tampilkan daftar perubahan konfigurasi baru menuju `stdout`, tanpa mengubah file `karabiner.json` yang sesungguhnya:

`goku --dry-run`

- Tampilkan hasil file konfigurasi yang baru menuju `stdout`, tanpa mengubah file `karabiner.json` yang sesungguhnya:

`goku --dry-run-all`

- Tampilkan informasi bantuan:

`goku --help`

- Tampilkan informasi versi:

`goku --version`
