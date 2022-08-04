---
layout: page
title: windows/chkdsk (Indonesia)
description: "Memeriksa dan mencari kesalahan dalam sebuah sistem file dan metadata volume penyimpanan."
content_hash: 64157280b9e8a2d1ffb7de35dfde2ec8f431acd2
related_topics:
  - title: English version
    url: /en/windows/chkdsk.html
    icon: bi bi-globe
---
# chkdsk

Memeriksa dan mencari kesalahan dalam sebuah sistem file dan metadata volume penyimpanan.
Informasi lebih lanjut: <https://docs.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Memeriksa sebuah ruang penyimpanan berdasarkan huruf drive (diakhiri dengan titik dua), lokasi pemasangan, atau nama ruang:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruang_penyimpanan</span>

- Memperbaiki kesalahan pada ruang penyimpanan yang ditentukan:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruang_penyimpanan</span>` /f`

- Melepas ruang penyimpanan tertentu untuk pemeriksaan:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruang_penyimpanan</span>` /x`

- Mengubah ukuran file log dalam sebuah ruang penyimpanan dengan sistem file NTFS:

`chkdsk /l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ukuran</span>
