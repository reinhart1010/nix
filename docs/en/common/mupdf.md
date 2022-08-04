---
layout: page
title: common/mupdf (English)
description: "MuPDF is a lightweight PDF, XPS, and E-book viewer."
content_hash: b4e85959d8177dc5ebe977e34e14222775aa28ff
---
# mupdf

MuPDF is a lightweight PDF, XPS, and E-book viewer.
More information: <https://www.mupdf.com>.

- Open a PDF on the first page:

`mupdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Open a PDF on page 3:

`mupdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Open a password secured PDF:

`mupdf -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Open a PDF with an initial zoom level, specified as DPI, of 72:

`mupdf -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">72</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Open a PDF with inverted color:

`mupdf -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Open a PDF tinted red #FF0000 (hexadecimal color syntax RRGGBB):

`mupdf -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FF0000</span>

- Open a PDF without anti-aliasing (0 = off, 8 = best):

`mupdf -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
