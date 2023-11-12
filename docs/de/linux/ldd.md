---
layout: page
title: linux/ldd (Deutsch)
description: "Zeigt Abhängigkeiten von dynamischen Bibliotheken an."
content_hash: a1292ed3bc2777e01f0b5083fb7c82a11cbee963
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/ldd.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ldd

Zeigt Abhängigkeiten von dynamischen Bibliotheken an.
Weitere Informationen: <https://manned.org/ldd>.

- Zeige Abhängigkeiten von dynamischen Bibliotheken einer Binärdatei an:

`ldd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>

- Zeige ungenutzte direkte Abhängigkeiten an:

`ldd -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>
