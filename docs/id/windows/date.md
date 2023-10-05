---
layout: page
title: windows/date (Indonesia)
description: "Menampilkan atau mengatur tanggal sistem."
content_hash: d1d09f937762ff81d57885906b3cf1ec7528c407
last_modified_at: 2023-10-05
related_topics:
  - title: English version
    url: /en/windows/date.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/date.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># date

Menampilkan atau mengatur tanggal sistem.
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/date>.

- Tampilkan tanggal sistem saat ini dan meminta untuk memasukkan tanggal baru (biarkan kosong agar tidak berubah):

`date`

- Tampilkan tanggal sistem saat ini tanpa meminta untuk memasukkan tanggal baru:

`date /t`

- Ubah tanggal sistem saat ini ke tanggal tertentu:

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bulan</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hari</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tahun</span>
