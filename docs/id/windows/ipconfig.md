---
layout: page
title: windows/ipconfig (Indonesia)
description: "Menampilkan dan mengatur konfigurasi jaringan dalam sistem operasi Windows."
content_hash: 38c6708fa21ba016b4db3734299aef9b6e7b1154
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/ipconfig.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/ipconfig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/ipconfig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ipconfig

Menampilkan dan mengatur konfigurasi jaringan dalam sistem operasi Windows.
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

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
