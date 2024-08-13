---
layout: page
title: osx/dmesg (Nederlands)
description: "Schrijf de kernelberichten naar `stdout`."
content_hash: bbf1a32146392e74fe6e547f664aa07815a21e16
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/osx/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Schrijf de kernelberichten naar `stdout`.
Meer informatie: <https://keith.github.io/xcode-man-pages/dmesg.8.html>.

- Toon kernelberichten:

`dmesg`

- Toon hoeveel fysiek geheugen beschikbaar is op dit systeem:

`dmesg | grep -i memory`

- Toon kernelberichten 1 pagina per keer:

`dmesg | less`
