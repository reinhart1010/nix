---
layout: page
title: windows/ipconfig (Indonesia)
description: "Tampilkan dan atur konfigurasi jaringan dalam sistem operasi Windows."
content_hash: bfa7fc6b0f212129c0ac650d99705dfad04387d3
last_modified_at: 2024-09-15
related_topics:
  - title: Deutsch version
    url: /de/windows/ipconfig.html
    icon: bi bi-globe
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
  - title: Nederlands version
    url: /nl/windows/ipconfig.html
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

Tampilkan dan atur konfigurasi jaringan dalam sistem operasi Windows.
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Tampilkan daftar seluruh adaptor jaringan yang terpasang:

`ipconfig`

- Tampilkan daftar adaptor jaringan secara rinci:

`ipconfig /all`

- Perbarui alamat IP suatu adaptor jaringan:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adaptor</span>

- Kosongkan alamat-alamat IP yang disetel dalam suatu adaptor jaringan:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adaptor</span>

- Tampilkan dafter informasi DNS yang disimpan dalam cache:

`ipconfig /displaydns`

- Kosongkan cache DNS:

`ipconfig /flushdns`
