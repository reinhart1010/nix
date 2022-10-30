---
layout: page
title: linux/fatlabel (polski)
description: "Ustawia lub pobiera informację o nazwie partycji FAT32."
content_hash: d86041575d7b7ae0458b7f379df7a812fefc8407
related_topics:
  - title: English version
    url: /en/linux/fatlabel.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/fatlabel.html
    icon: bi bi-globe
---
# fatlabel

Ustawia lub pobiera informację o nazwie partycji FAT32.
Więcej informacji: <https://manned.org/fatlabel>.

- Pobranie informacji o nazwie partycji FAT32:

`fatlabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- Ustawienie nazwy partycji FAT32:

`fatlabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdc3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nowa_etykieta</span>`"`
