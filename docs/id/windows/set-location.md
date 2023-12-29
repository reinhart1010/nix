---
layout: page
title: windows/set-location (Indonesia)
description: "Tampilkan direktori kerja saat ini atau pindah ke direktori lain."
content_hash: 0f56a127d3fd3ac4a49f3b09de1bff537a912b69
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/windows/set-location.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/set-location.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Set-Location

Tampilkan direktori kerja saat ini atau pindah ke direktori lain.
Perintah ini hanya dapat digunakan dalam PowerShell.
Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- Pergi menuju suatu direktori pada drive yang sama:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\direktori</span>

- Pergi menuju direktori tertentu pada drive yang berbeda:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\direktori</span>

- Pergi dan tampilkan lokasi lengkap (absolute path) atas direktori yang dituju:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\direktori</span>` -PassThru`

- Pergi menuju induk dari direktori dari saat ini:

`Set-Location ..`

- Pergi menuju direktori pangkal/home milik pengguna saat ini:

`Set-Location ~`

- Pergi menuju direktori yang telah dikunjungi sebelumnya/setelahnya:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-|+</span>

- Pergi menuju akar (root) dari drive saat ini:

`Set-Location \`
