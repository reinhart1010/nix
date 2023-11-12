---
layout: page
title: common/head (Deutsch)
description: "Gibt den ersten Teil einer Datei aus."
content_hash: 69044aaa34eaa730451d04046d026d724d4878df
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/head.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/head.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/head.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/head.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/head.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># head

Gibt den ersten Teil einer Datei aus.
Weitere Informationen: <https://manned.org/head.1p>.

- Gib die ersten paar Zeilen einer Datei aus:

`head -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_zeilen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Gib die ersten Bytes einer Datei aus:

`head -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Gib alle bis auf die letzten Zeilen einer Datei aus:

`head -n -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_zeilen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Gib alle bis auf die letzten Bytes einer Datei aus:

`head -c -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>
