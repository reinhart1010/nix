---
layout: page
title: linux/blkid (polski)
description: "Wyświetla wszystkie rozpoznane partycje oraz ich Universally Unique Identifier (UUID)."
content_hash: 03c5abec9a8b9e91b914e702796535e1555bbc35
related_topics:
  - title: English version
    url: /en/linux/blkid.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/blkid.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/blkid.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># blkid

Wyświetla wszystkie rozpoznane partycje oraz ich Universally Unique Identifier (UUID).
Więcej informacji: <https://manned.org/blkid>.

- Wyświetlenie wszystkich partycji:

`sudo blkid`

- Wyświetlenie wszystkich partycji w tabeli, wraz z bieżącymi punktami montowania:

`sudo blkid -o list`
