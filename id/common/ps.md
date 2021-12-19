---
layout: page
title: common/ps (Indonesia)
description: "Informasi tentang proses-proses yang berlangsung."
content_hash: 3845ca8eac4ffa57ef19c1e492b1fc7834a4ec18
related_topics:
  - title: English version
    url: /en/common/ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ps.html
    icon: bi bi-globe
---
# ps

Informasi tentang proses-proses yang berlangsung.

- Menampilkan daftar semua proses yang berlangsung:

`ps aux`

- Menampilkan daftar semua proses yang berlangsung termasuk _string_ perintah secara utuh:

`ps auxww`

- Mencari proses yang sesuai dengan _string_:

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Menampilkan daftar semua proses pengguna yang berlangsung dengan format tambahan yang utuh:

`ps --user $(id -u) -F`

- Menampilkan daftar semua proses pengguna yang berlangsung sebagai pohon:

`ps --user $(id -u) f`

- Mengambil induk PID dari sebuah proses:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Sortir proses berdasarkan konsumsi memori:

`ps --sort size`
