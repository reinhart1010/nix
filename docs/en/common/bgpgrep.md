---
layout: page
title: common/bgpgrep (English)
description: "Filter and print BGP data within MRT dumps."
content_hash: c0c2ce3b504dbe8fdb36dfb2c22a7b22c80a70fe
last_modified_at: 2023-06-23
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bgpgrep

Filter and print BGP data within MRT dumps.
Can read files compressed with gzip, bzip2 and xz.
More information: <https://gitea.it/1414codeforge/ubgpsuite>.

- Output all routes:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>

- Output all routes received from a specific peer, determined by the peer's AS number:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master4.mrt</span>` -peer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64498</span>

- Output all routes received from a specific peer, determined by the peer's IP address:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master4.mrt.bz2</span>` -peer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:cafe:acd::19e</span>

- Output all routes which have certain ASNs in their AS path:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt.bz2</span>` -aspath '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64498 64510</span>`'`

- Output all routes that lead to a specific address:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt.bz2</span>` -supernet '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:cafe:aef::5</span>`'`

- Output all routes that have communities from a specific AS:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master4.mrt</span>` -communities \( '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64497</span>`:*' \)`
