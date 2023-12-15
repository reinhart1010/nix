---
layout: page
title: windows/chkdsk (Indonesia)
description: "Periksa kesalahan dalam sistem file dan metadata volume penyimpanan."
content_hash: 4f52f35bf622e0966ad63031e6b2b24a8722b30e
last_modified_at: 2023-12-15
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

Periksa kesalahan dalam sistem file dan metadata volume penyimpanan.
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Periksa sebuah ruang penyimpanan berdasarkan huruf drive (diakhiri dengan titik dua), lokasi pemasangan, atau nama ruang:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruang_penyimpanan</span>

- Perbaiki kesalahan pada ruang penyimpanan yang ditentukan:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruang_penyimpanan</span>` /f`

- Lepaskan ruang penyimpanan tertentu untuk pemeriksaan:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruang_penyimpanan</span>` /x`

- Ubah ukuran file log dalam sebuah ruang penyimpanan dengan sistem file NTFS:

`chkdsk /l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ukuran</span>
