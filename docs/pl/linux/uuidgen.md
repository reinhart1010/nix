---
layout: page
title: linux/uuidgen (polski)
description: "Stwórz unikalny identyfikator (UUIDs)."
content_hash: 4e7413928794c5eee888bdebd65db6d4633a0b2c
related_topics:
  - title: English version
    url: /en/linux/uuidgen.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># uuidgen

Stwórz unikalny identyfikator (UUIDs).
Zobacz też `uuid`.
Więcej informacji: <https://manned.org/uuidgen>.

- Stwórz losowy UUIDv4:

`uuidgen --random`

- Stwórz UUIDv1 oparty o aktualny czas:

`uuidgen --time`

- Stwórz UUIDv5 z nazwy i prefiksu przestrzeni nazw:

`uuidgen --sha1 --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@dns|@url|@oid|@x500</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_obiektu</span>
