---
layout: page
title: windows/cd (Indonesia)
description: "Tampilkan direktori kerja saat ini atau pindah ke direktori lain."
content_hash: 5149014519c3bdb095a8046ac9efa993c1769840
last_modified_at: 2023-11-26
related_topics:
  - title: বাংলা version
    url: /bn/windows/cd.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/cd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/cd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/cd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cd.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/cd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cd

Tampilkan direktori kerja saat ini atau pindah ke direktori lain.
Dalam PowerShell, perintah ini merupakan alias dari `Set-Location`. Dokumentasi ini ditulis menurut perintah `cd` versi Command Prompt (`cmd`).
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- Lihat dokumentasi untuk perintah PowerShell serupa:

`tldr set-location`

- Tampilkan nama dari direktori saat ini:

`cd`

- Pergi menuju suatu direktori pada drive yang sama:

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\direktori</span>

- Pergi menuju direktori tertentu pada [d]rive yang berbeda:

`cd /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\direktori</span>

- Pergi menuju induk dari direktori dari saat ini:

`cd ..`

- Pergi menuju direktori pangkal/home milik pengguna saat ini:

`cd %userprofile%`

- Pergi menuju akar (root) dari drive saat ini:

`cd \`
