---
layout: page
title: windows/find (Indonesia)
description: "Mencari teks tertentu di dalam suatu file atau direktori."
content_hash: 8031a5e27023dc3695ad1c710801eecad3574971
last_modified_at: 2023-12-29
related_topics:
  - title: বাংলা version
    url: /bn/windows/find.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/find.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/find.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/find.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/find.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/find.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/find.html
    icon: bi bi-globe
tldri18n_status: 2
---
# find

Mencari teks tertentu di dalam suatu file atau direktori.
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Mencari baris-baris dalam file yang mengandung teks tertentu:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">teks</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>

- Menunjukkan baris-baris dalam file yang tidak mengandung teks tertentu:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">teks</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>` /v`

- Menghitung jumlah baris dalam file yang mengandung teks tertentu:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">teks</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>` /c`

- Mencari baris-baris dalam file yang mengandung teks tertentu beserta nomor barisnya:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">teks</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>` /n`
