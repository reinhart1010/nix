---
layout: page
title: common/peerindex (English)
description: "Inspect MRT TABLE_DUMPV2 Peer Index Table."
content_hash: b78b2145c9e0dcfc128d660a9bd0057d751a4719
last_modified_at: 2023-06-23
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># peerindex

Inspect MRT TABLE_DUMPV2 Peer Index Table.
Can read files compressed with gzip, bzip2 and xz.
More information: <https://gitea.it/1414codeforge/ubgpsuite>.

- Output all peers:

`peerindex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>

- Display all peers that have provided routing information:

`peerindex -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>
