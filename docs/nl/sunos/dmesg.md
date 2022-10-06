---
layout: page
title: sunos/dmesg (Nederlands)
description: "Schrijft de kernel berichten naar de standaard output."
content_hash: 235169e50b79099fa32cdc50890951873ff2bb8a
related_topics:
  - title: English version
    url: /en/sunos/dmesg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/sunos/dmesg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dmesg

Schrijft de kernel berichten naar de standaard output.
Meer informatie: <https://www.unix.com/man-page/sunos/1m/dmesg>.

- Toont kernel berichten:

`dmesg`

- Toont hoeveel fysiek geheugen beschikbaar is op het systeem:

`dmesg | grep -i memory`

- Toont kernel berichten per pagina:

`dmesg | less`
