---
layout: page
title: windows/curl (Indonesia)
description: "Perintah ini dapat merupakan alias dari `Invoke-WebRequest` jika program `curl` (<https://curl.se>) tidak terpasang secara benar di PowerShell."
content_hash: e667952f8aea8f526d0c616004b8769d4058b8a8
related_topics:
  - title: English version
    url: /en/windows/curl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/curl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># curl

Perintah ini dapat merupakan alias dari `Invoke-WebRequest` jika program `curl` (<https://curl.se>) tidak terpasang secara benar di PowerShell.

- Cari tahu apakah `curl` sudah terpasang dengan benar dengan menampilkan versi program tersebut. Jika perintah ini memunculkan pesan galat/error, maka PowerShell berkemungkinan sedang menggantinya dengan `Invoke-WebRequest`:

`curl --version`

- Tampilkan dokumentasi untuk perintah `curl` yang asli:

`tldr curl -p common`

- Tampilkan dokumentasi untuk perintah `curl` yang asli dalam program `tldr` versi lawas:

`tldr curl -o common`

- Tampilkan dokumentasi untuk perintah `Invoke-WebRequest`:

`tldr invoke-webrequest`
