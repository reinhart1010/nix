---
layout: page
title: common/acyclic (Indonesia)
description: "Jadikan gambaran grafik berarah (dalam Graphviz) menjadi asiklik dengan memutarbalikkan beberapa garis tepi."
content_hash: a17d3a4953984e9a2fe4997dd6fc04e3ec145763
last_modified_at: 2023-12-15
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
  - title: 한국어 version
    url: /ko/common/acyclic.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acyclic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acyclic.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/acyclic.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># acyclic

Jadikan gambaran grafik berarah (dalam Graphviz) menjadi asiklik dengan memutarbalikkan beberapa garis tepi.
Daftar filter Graphviz: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
Informasi lebih lanjut: <https://graphviz.org/pdf/acyclic.1.pdf>.

- Ubah grafik berarah menjadi asiklik dengan membalikkan beberapa garis tepi:

`acyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Cari tahu apakah grafik tersebut bersifat asiklik, memiliki siklus, atau tidak berarah, sehingga tidak menghasilkan output:

`acyclic -v -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>

- Tampilkan informasi bantuan untuk `acyclic`:

`acyclic -?`
