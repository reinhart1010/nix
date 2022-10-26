---
layout: page
title: linux/uuidd (polski)
description: "Daemon generujący UUID."
content_hash: 726cecd9e4c2982340f54ed3a8806f7e23e9682c
related_topics:
  - title: English version
    url: /en/linux/uuidd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># uuidd

Daemon generujący UUID.
Więcej informacji: <https://manned.org/uuidd>.

- Stwórz losowy UUID:

`uuidd --random`

- Stwórz większą ilość losowych UUID:

`uuidd --random --uuids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ilość_uuid</span>

- Stwórz UUID oparty o aktualny czas i adres MAC:

`uuidd --time`
