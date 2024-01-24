---
layout: page
title: common/pnmtosgi (English)
description: "Convert a PNM file to an SGI image file."
content_hash: 4d47c0d85b6c98e59edefb9d024ca464ed360319
last_modified_at: 2024-01-24
tldri18n_status: 2
---
# pnmtosgi

Convert a PNM file to an SGI image file.
More information: <https://netpbm.sourceforge.net/doc/pnmtosgi.html>.

- Convert a PNM image to an SGI image:

`pnmtosgi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.sgi</span>

- Disable or enable compression:

`pnmtosgi -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verbatim|rle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.sgi</span>

- Write the specified string into the SGI image header's `imagename` field:

`pnmtosgi -imagename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.sgi</span>
