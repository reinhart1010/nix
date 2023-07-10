---
layout: page
title: common/peerindex (Deutsch)
description: "Liest MRT TABLE_DUMPV2 Peer Index Table aus."
content_hash: 5d20c42058c95381013b5f4c26cb14430bbbb1c7
last_modified_at: 2023-07-10
related_topics:
  - title: English version
    url: /en/common/peerindex.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># peerindex

Liest MRT TABLE_DUMPV2 Peer Index Table aus.
Kann mit gzip, bzip2 und xz komprimierte Dateien lesen.
Weitere Informationen: <https://gitea.it/1414codeforge/ubgpsuite>.

- Gib alle Peers aus:

`peerindex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>

- Zeige alle Peers an, die Routing-Informationen bereitgestellt haben:

`peerindex -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>
