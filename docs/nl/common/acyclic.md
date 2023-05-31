---
layout: page
title: common/acyclic (Nederlands)
description: "Maak een gerichte grafiek acyclisch door enkele randen om te keren."
content_hash: 17c5686543451cdfc770e0f021dc462be134e3be
last_modified_at: 2023-05-31
related_topics:
  - title: English version
    url: /en/common/acyclic.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acyclic.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acyclic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acyclic.html
    icon: bi bi-globe
---
# acyclic

Maak een gerichte grafiek acyclisch door enkele randen om te keren.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
Meer informatie: <https://graphviz.org/pdf/acyclic.1.pdf>.

- Maak een gerichte grafiek acyclisch door enkele randen om te keren:

`acyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.gv</span>

- Afdrukken als een grafiek acyclisch is, een cyclus heeft of ongericht is en geen uitvoergrafiek produceert:

`acyclic -v -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.gv</span>

- Hulp weergeven voor `acyclic`:

`acyclic -?`
