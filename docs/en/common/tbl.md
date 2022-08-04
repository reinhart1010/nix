---
layout: page
title: common/tbl (English)
description: "Table preprocessor for the groff (GNU Troff) document formatting system."
content_hash: ae7cfb065797710cea155df3af3978d7f24b3091
---
# tbl

Table preprocessor for the groff (GNU Troff) document formatting system.
See also `groff` and `troff`.
More information: <https://manned.org/tbl>.

- Process input with tables, saving the output for future typesetting with groff to PostScript:

`tbl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.roff</span>

- Typeset input with tables to PDF using the [me] macro package:

`tbl -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tbl</span>` | groff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>
