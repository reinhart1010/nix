---
layout: page
title: sunos/devfsadm (Nederlands)
description: "Administratie commando voor `/dev`. Beheert de `/dev` namespace."
content_hash: 324278ee2f2879d062c91518ecf3888ce64db4cc
related_topics:
  - title: English version
    url: /en/sunos/devfsadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/devfsadm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># devfsadm

Administratie commando voor `/dev`. Beheert de `/dev` namespace.
Meer informatie: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Scannen voor nieuwe schijven:

`devfsadm -c disk`

- Opkuisen van overblijvende /dev links, en detectie van nieuwe toestellen:

`devfsadm -C -v`

- Dry-run - output van wat er zou veranderen, zonder deze door te voeren:

`devfsadm -C -v -n`
