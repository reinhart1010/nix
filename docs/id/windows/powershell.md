---
layout: page
title: windows/powershell (Indonesia)
description: "Sebuah syel/shell dan bahasa pemrograman berbasis naskah/script yang dirancang untuk administrasi sistem komputer."
content_hash: 87dd9190f5780dc43fec869ae2e74ab6a7f64745
last_modified_at: 2023-12-15
related_topics:
  - title: English version
    url: /en/windows/powershell.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/powershell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># powershell

Sebuah syel/shell dan bahasa pemrograman berbasis naskah/script yang dirancang untuk administrasi sistem komputer.
Perintah ini merujuk kepada PowerShell versi 5.1 ke bawah (juga dikenal sebagai PowerShell bawaan Windows). Gunakan perintah `pwsh` daripada `powershell` untuk menggunakan PowerShell versi terkini (6.0 ke atas) yang tersedia lintas sistem operasi.
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Jalankan sesi PowerShell interaktif baru:

`powershell`

- Jalankan sesi interaktif tanpa memuat profil konfigurasi startup:

`powershell -NoProfile`

- Jalankan perintah secara spesifik:

`powershell -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'powershell telah dieksekusi'</span>`"`

- Jalankan suatu naskah perintah/script PowerShell:

`powershell -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/naskah.ps1</span>

- Jalankan suatu sesi dengan versi PowerShell tertentu:

`powershell -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Cegah sesi PowerShell dari keluar secara otomatis setelah menjalankan perintah startup:

`powershell -NoExit`

- Tentukan format data yang akan dimasukkan ke dalam PowerShell:

`powershell -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- Tentukan format data yang ingin dikeluarkan dari perintah-perintah PowerShell:

`powershell -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
