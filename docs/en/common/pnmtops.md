---
layout: page
title: common/pnmtops (English)
description: "Convert a PNM image to a PostScript file."
content_hash: 1fbfaf693014a0aeba2f4418155357b36ab43bda
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# pnmtops

Convert a PNM image to a PostScript file.
More information: <https://netpbm.sourceforge.net/doc/pnmtops.html>.

- Convert a PNM image to a PS file:

`pnmtops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ps</span>

- Specify the dimensions of the output image in inches:

`pnmtops -imagewidth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagewidth</span>` -imageheight `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imageheight</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ps</span>

- Specify the dimensions of the page the output image resides on in inches:

`pnmtops -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ps</span>
