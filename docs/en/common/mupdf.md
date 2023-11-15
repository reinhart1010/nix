---
layout: page
title: common/mupdf (English)
description: "A lightweight PDF, XPS, and E-book viewer."
content_hash: 998ec483b7e1a067c5e80c85de2a8852213a85fe
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# mupdf

A lightweight PDF, XPS, and E-book viewer.
More information: <https://www.mupdf.com>.

- Open a PDF on the first page:

`mupdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a PDF on page 3:

`mupdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Open a password secured PDF:

`mupdf -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a PDF with an initial zoom level, specified as DPI, of 72:

`mupdf -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">72</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a PDF with inverted color:

`mupdf -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a PDF tinted red #FF0000 (hexadecimal color syntax RRGGBB):

`mupdf -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FF0000</span>

- Open a PDF without anti-aliasing (0 = off, 8 = best):

`mupdf -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
