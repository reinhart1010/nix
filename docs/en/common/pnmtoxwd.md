---
layout: page
title: common/pnmtoxwd (English)
description: "Convert a PNM file into an X11 window dump file."
content_hash: 30ca7edf22b98832380ad8b9686c08b94241e6a9
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# pnmtoxwd

Convert a PNM file into an X11 window dump file.
More information: <https://netpbm.sourceforge.net/doc/pnmtoxwd.html>.

- Convert a PNM image file to XWD:

`pnmtoxwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xwd</span>

- Produce the output in the DirectColor format:

`pnmtoxwd -directcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xwd</span>

- Set the color depth of the output to b bits:

`pnmtoxwd -pseudodepth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xwd</span>
