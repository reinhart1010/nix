---
layout: page
title: windows/xcopy (Indonesia)
description: "Membuat salinan file dan direktori."
content_hash: a84b30c7f84953a7672e89c8ce356a0fab05ca45
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/xcopy.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/xcopy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/xcopy.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/xcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/xcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcopy

Membuat salinan file dan direktori.
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Membuat salinan file atau direktori ke lokasi lain:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_tujuan</span>

- Melihat daftar file yang akan disalin sebelum proses salinan dimulai:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_tujuan</span>` /p`

- Membuat salinan struktur direktori saja (tanpa file di dalamnya):

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_tujuan</span>` /t`

- Membuat salinan direktori termasuk direktori-direktori kosong (tanpa file):

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_tujuan</span>` /e`

- Membuat salinan file atau direktori dengan daftar hak akses pengguna (ACL) yang sama:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_tujuan</span>` /o`

- Mempersilakan proses penyalinan file atau direktori saat koneksi jaringan komputer terputus:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_tujuan</span>` /z`

- Mempersilakan `xcopy` untuk tetap mengganti file yang sudah ada di lokasi tujuan dengan file yang berada di lokasi sumber:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_tujuan</span>` /y`

- Menampilkan cara penggunaan secara lengkap:

`xcopy /?`
