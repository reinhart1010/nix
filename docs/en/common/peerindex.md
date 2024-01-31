---
layout: page
title: common/peerindex (English)
description: "Inspect MRT TABLE_DUMPV2 Peer Index Table."
content_hash: 71fb78fd0df6ba0748df77f488ce1273814951d7
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/common/peerindex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# peerindex

Inspect MRT TABLE_DUMPV2 Peer Index Table.
Can read files compressed with `gzip`, `bzip2` and `xz`.
More information: <https://codeberg.org/1414codeforge/ubgpsuite>.

- List all peers:

`peerindex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>

- Display all peers that have provided routing information:

`peerindex -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>
