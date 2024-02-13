---
layout: page
title: common/pbmtoescp2 (English)
description: "Convert a PBM image to a ESC/P2 printer file."
content_hash: b5988ac64bcecb1b21a9bd1eab62d168478da1a2
last_modified_at: 2024-02-13
tldri18n_status: 2
---
# pbmtoescp2

Convert a PBM image to a ESC/P2 printer file.
See also: `pbmtoepson`, `escp2topbm`.
More information: <https://netpbm.sourceforge.net/doc/pbmtoescp2.html>.

- Convert a PBM image to a ESC/P2 printer file:

`pbmtoescp2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.escp2</span>

- Specify the compression of the output:

`pbmtoescp2 -compression `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.escp2</span>

- Specify the horizontal and vertical resolution of the output in dots per inch:

`pbmtoescp2 -resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">180|360|720</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.escp2</span>

- Place a formfeed command at the end of the output:

`pbmtoescp2 -formfeed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.escp2</span>
