---
layout: page
title: osx/caffeinate (Indonesia)
description: "Menghindari macOS dari sleep (mode tidur)."
content_hash: 30b796b374337c766b74fb73b714d394e2046092
related_topics:
  - title: Deutsch version
    url: /de/osx/caffeinate.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/caffeinate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/caffeinate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/caffeinate.html
    icon: bi bi-globe
---
# caffeinate

Menghindari macOS dari sleep (mode tidur).
Informasi lebih lanjut: <https://ss64.com/osx/caffeinate.html>.

- Menghindari mode sleep selama 1 jam (3600 detik):

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Menghindari mode sleep sampai sebuah command selesai:

`caffeinate -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Menghindari mode sleep sampai anda mengetik Ctrl-C:

`caffeinate -i`
