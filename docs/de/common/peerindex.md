---
layout: page
title: common/peerindex (Deutsch)
description: "Liest MRT TABLE_DUMPV2 Peer Index Table aus."
content_hash: b71e0c6a0cc9b0bfc397f62bf63264f1f1d777c4
last_modified_at: 2023-07-11
related_topics:
  - title: English version
    url: /en/common/peerindex.html
    icon: bi bi-globe
---
# peerindex

Liest MRT TABLE_DUMPV2 Peer Index Table aus.
Kann mit gzip, bzip2 und xz komprimierte Dateien lesen.
Weitere Informationen: <https://codeberg.org/1414codeforge/ubgpsuite>.

- Gib alle Peers aus:

`peerindex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>

- Zeige alle Peers an, die Routing-Informationen bereitgestellt haben:

`peerindex -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>
