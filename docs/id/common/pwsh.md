---
layout: page
title: common/pwsh (Indonesia)
description: "Sebuah syel/shell dan bahasa pemrograman berbasis naskah/script yang dirancang untuk administrasi sistem komputer."
content_hash: 2916ac21b11b68f7b2a037cafa778175f20f8ca5
last_modified_at: 2023-12-15
related_topics:
  - title: English version
    url: /en/common/pwsh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pwsh.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/pwsh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pwsh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pwsh

Sebuah syel/shell dan bahasa pemrograman berbasis naskah/script yang dirancang untuk administrasi sistem komputer.
Perintah ini merujuk kepada PowerShell versi 6 ke atas (juga dikenal sebagai PowerShell Core dan PowerShell lintas sistem operasi). Gunakan perintah `powershell` daripada `pwsh` untuk menggunakan PowerShell versi bawaan Windows (5.1 ke bawah).
Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

- Jalankan sesi PowerShell interaktif baru:

`pwsh`

- Jalankan sesi interaktif tanpa memuat profil konfigurasi startup:

`pwsh -NoProfile`

- Jalankan perintah secara spesifik:

`pwsh -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'powershell telah dieksekusi'</span>`"`

- Jalankan suatu naskah perintah/script PowerShell:

`pwsh -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/naskah.ps1</span>

- Jalankan suatu sesi dengan versi PowerShell tertentu:

`pwsh -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Cegah sesi PowerShell dari keluar secara otomatis setelah menjalankan perintah startup:

`pwsh -NoExit`

- Tentukan format data yang akan dimasukkan ke dalam PowerShell:

`pwsh -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- Tentukan format data yang ingin dikeluarkan dari perintah-perintah PowerShell:

`pwsh -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
