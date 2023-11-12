---
layout: page
title: windows/chkdsk (Indonesia)
description: "Memeriksa dan mencari kesalahan dalam sebuah sistem file dan metadata volume penyimpanan."
content_hash: 0bcdca49e5150620d5ff0642d5d0161c4d137462
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/chkdsk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/chkdsk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/chkdsk.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/chkdsk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chkdsk

Memeriksa dan mencari kesalahan dalam sebuah sistem file dan metadata volume penyimpanan.
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Memeriksa sebuah ruang penyimpanan berdasarkan huruf drive (diakhiri dengan titik dua), lokasi pemasangan, atau nama ruang:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruang_penyimpanan</span>

- Memperbaiki kesalahan pada ruang penyimpanan yang ditentukan:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruang_penyimpanan</span>` /f`

- Melepas ruang penyimpanan tertentu untuk pemeriksaan:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruang_penyimpanan</span>` /x`

- Mengubah ukuran file log dalam sebuah ruang penyimpanan dengan sistem file NTFS:

`chkdsk /l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ukuran</span>
