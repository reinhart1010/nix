---
layout: page
title: common/grap (English)
description: "A charting preprocessor for the groff (GNU Troff) document formatting system."
content_hash: 078ddd084aa1b5bf9d1529ddedc1fe1b03006d85
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# grap

A charting preprocessor for the groff (GNU Troff) document formatting system.
See also `pic` and `groff`.
More information: <https://manned.org/grap>.

- Process a `grap` file and save the output file for future processing with `pic` and `groff`:

`grap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.grap</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pic</span>

- Typeset a `grap` file to PDF using the [me] macro package, saving the output to a file:

`grap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.grap</span>` | pic -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` | groff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>
