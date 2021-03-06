---
layout: page
title: windows/ipconfig (Indonesia)
description: "Menampilkan dan mengatur konfigurasi jaringan dalam sistem operasi Windows."
content_hash: 8497110e3d288305346145d36659c2f78b46335a
related_topics:
  - title: English version
    url: /en/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
---
# ipconfig

Menampilkan dan mengatur konfigurasi jaringan dalam sistem operasi Windows.
Informasi lebih lanjut: <https://docs.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Menunjukkan daftar adaptor jaringan:

`ipconfig`

- Menunjukkan daftar adaptor jaringan secara lengkap:

`ipconfig /all`

- Memperbarui alamat IP sebuah adaptor jaringan:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adaptor</span>

- Mengosongkan alamat-alamat IP yang disetel dalam sebuah adaptor jaringan:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adaptor</span>

- Mengosongkan cache DNS:

`ipconfig /flushdns`
