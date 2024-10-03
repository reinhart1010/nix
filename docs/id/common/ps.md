---
layout: page
title: common/ps (Indonesia)
description: "Tampilkan informasi tentang proses-proses yang berlangsung."
content_hash: d232f2f206e1a798060ccdbe4f8eb8b8184e8c70
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/ps.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ps.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ps.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ps.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

Tampilkan informasi tentang proses-proses yang berlangsung.
Informasi lebih lanjut: <https://manned.org/ps>.

- Tampilkan daftar seluruh proses yang berlangsung:

`ps aux`

- Tampilkan daftar seluruh proses yang berlangsung termasuk string perintah secara utuh:

`ps auxww`

- Cari proses berdasarkan teks/string kriteria (penambahan kurung siku akan mencegah `grep` untuk mencocokkan dirinya sendiri):

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[s]tring</span>

- Tampilkan daftar seluruh proses dari pengguna saat ini dengan format tambahan ekstra:

`ps --user $(id -u) -F`

- Tampilkan daftar seluruh proses dari pengguna saat ini dalam format pohon:

`ps --user $(id -u) f`

- Mengambil induk PID dari sebuah proses:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Sortir proses berdasarkan konsumsi memori:

`ps --sort size`
