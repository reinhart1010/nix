---
layout: page
title: windows/wget (Indonesia)
description: "Perintah ini dapat merupakan alias dari `Invoke-WebRequest` jika program `wget` (<https://www.gnu.org/software/wget>) tidak terpasang secara benar di PowerShell."
content_hash: d451a723d1eea415536fbe9aa3f90a54331eb4cf
related_topics:
  - title: English version
    url: /en/windows/wget.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># wget

Perintah ini dapat merupakan alias dari `Invoke-WebRequest` jika program `wget` (<https://www.gnu.org/software/wget>) tidak terpasang secara benar di PowerShell.

- Cari tahu apakah `wget` sudah terpasang dengan benar dengan menampilkan versi program tersebut. Jika perintah ini memunculkan pesan galat/error, maka PowerShell berkemungkinan sedang menggantinya dengan `Invoke-WebRequest`:

`curl --version`

- Tampilkan dokumentasi untuk perintah `wget` yang asli:

`tldr wget -p common`

- Tampilkan dokumentasi untuk perintah `wget` yang asli dalam program `tldr` versi lawas:

`tldr wget -o common`

- Tampilkan dokumentasi untuk perintah `Invoke-WebRequest`:

`tldr invoke-webrequest`
