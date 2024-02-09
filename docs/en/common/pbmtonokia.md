---
layout: page
title: common/pbmtonokia (English)
description: "Convert a PBM image to one of Nokia's Smart Messaging Formats ."
content_hash: 66dffef2c888bf8a523c423461ffa30d13c19521
last_modified_at: 2024-02-09
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtonokia.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtonokia

Convert a PBM image to one of Nokia's Smart Messaging Formats .
More information: <https://netpbm.sourceforge.net/doc/pbmtonokia.html>.

- Convert a PBM image into a Nokia Operator Logo as hexcode:

`pbmtonokia -fmt NEX_NOL -net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_operator_code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.hex</span>

- Convert a PBM image into a Nokia Group Graphic as hexcode:

`pbmtonokia -fmt NEX_NGG `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.hex</span>

- Convert a PBM image into a Nokia Picture Message with the specified text as hexcode:

`pbmtonokia -fmt NEX_NPM -txt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text_message</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.hex</span>

- Convert a PBM image into a Nokia Operator Logo as a NOL file:

`pbmtonokia -fmt NOL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.nol</span>

- Convert a PBM image into a Nokia Group Graphic as an NGG file:

`pbmtonokia -fmt NGG `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ngg</span>

- Convert a PBM image into a Nokia Picture Message as an NPM file:

`pbmtonokia -fmt NPM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.npm</span>
