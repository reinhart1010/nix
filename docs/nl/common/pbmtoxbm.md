---
layout: page
title: common/pbmtoxbm (Nederlands)
description: "Converteer een PBM image naar een X11 of X10 bitmap."
content_hash: c4eeca8cfa265c3f0ba8d19d14bfb6584c5365d0
last_modified_at: 2023-12-18
related_topics:
  - title: English version
    url: /en/common/pbmtoxbm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtoxbm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtoxbm

Converteer een PBM image naar een X11 of X10 bitmap.
Meer informatie: <https://netpbm.sourceforge.net/doc/pbmtoxbm.html>.

- Converteer een PPM image naar een X11 XBM bestand:

`pbmtoxbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.xbm</span>

- Specificeer expliciet of een X11 of X10 bitmap gegenereerd moet worden:

`pbmtoxbm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11|x10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.xbm</span>
