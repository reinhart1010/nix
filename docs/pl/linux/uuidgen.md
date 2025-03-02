---
layout: page
title: linux/uuidgen (polski)
description: "Stwórz unikalny identyfikator (UUIDs)."
content_hash: 030f637b7dfd7dde808f6528c56d2554253dd723
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/uuidgen.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/uuidgen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uuidgen

Stwórz unikalny identyfikator (UUIDs).
Zobacz także `uuid`.
Więcej informacji: <https://manned.org/uuidgen>.

- Stwórz losowy UUIDv4:

`uuidgen --random`

- Stwórz UUIDv1 oparty o aktualny czas:

`uuidgen --time`

- Stwórz UUIDv5 z nazwy i prefiksu przestrzeni nazw:

`uuidgen --sha1 --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@dns|@url|@oid|@x500</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_obiektu</span>
