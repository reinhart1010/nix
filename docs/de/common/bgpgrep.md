---
layout: page
title: common/bgpgrep (Deutsch)
description: "Filtert und gibt BGP-Daten in einem MRT-Dump aus."
content_hash: 27a91ef973927c189475ff437be51d043babe039
last_modified_at: 2023-07-11
related_topics:
  - title: English version
    url: /en/common/bgpgrep.html
    icon: bi bi-globe
---
# bgpgrep

Filtert und gibt BGP-Daten in einem MRT-Dump aus.
Kann mit gzip, bzip2 und xz komprimierte Dateien lesen.
Weitere Informationen: <https://codeberg.org/1414codeforge/ubgpsuite>.

- Gib alle Routen aus:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>

- Gib alle von einem bestimmten Peer empfangenen Routen aus, bestimmt durch die AS-Nummer des Peers:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master4.mrt</span>` -peer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64498</span>

- Gib alle von einem bestimmten Peer empfangenen Routen aus, bestimmt durch die IP-Adresse des Peers:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master4.mrt.bz2</span>` -peer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:cafe:acd::19e</span>

- Gib alle Routen aus, die bestimmte ASNs in ihrem AS-Pfad haben:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt.bz2</span>` -aspath '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64498 64510</span>`'`

- Gib Routen aus, die zu einer bestimmten Adresse führen:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt.bz2</span>` -supernet '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:cafe:aef::5</span>`'`

- Gib alle Routen aus, die Communities von einem bestimmten AS haben:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master4.mrt</span>` -communities \( '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64497</span>`:*' \)`
