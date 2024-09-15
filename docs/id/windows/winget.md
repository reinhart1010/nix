---
layout: page
title: windows/winget (Indonesia)
description: "Manajer Paket Antarmuka Baris Perintah Windows."
content_hash: 60f81df17df9261f88594c17672f6a9b3ec2ea05
last_modified_at: 2024-09-15
related_topics:
  - title: Deutsch version
    url: /de/windows/winget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/winget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/winget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/winget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/winget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/winget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/winget.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># winget

Manajer Paket Antarmuka Baris Perintah Windows.
Informasi lebih lanjut: <https://learn.microsoft.com/windows/package-manager/winget>.

- Pasang suatu paket:

`winget install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus paket yang terpasang sebelumnya (Catatan: subperintah `uninstall` juga dapat digantikan dengan `remove`):

`winget uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Tampilkan informasi tentang paket:

`winget show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Cari paket:

`winget search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Perbarui seluruh paket menuju versi terkini:

`winget upgrade --all`

- Tampilkan paket terpasang yang dapat dikelola oleh `winget`:

`winget list --source winget`

- Impor atau ekspor daftar paket terpasang ke dalam suatu file:

`winget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import|export</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--import-file|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Lakukan uji validasi manifes pemaketan winget sebelum mengirimkan rencana perubahan (Pull Request) menuju repositori winget-pkgs:

`winget validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/manifes</span>
