---
layout: page
title: common/pnmquantall (English)
description: "Run `pnmquant` on multiple files at once such that they share a common colormap."
content_hash: 10483ab1d352f7f44609ce80493ffe062b6f55f2
last_modified_at: 2024-03-03
tldri18n_status: 2
---
# pnmquantall

Run `pnmquant` on multiple files at once such that they share a common colormap.
See also: `pnmquant`.
More information: <https://netpbm.sourceforge.net/doc/pnmquantall.html>.

- Run `pnmquant` on multiple files with the specified parameters, overwriting the original files:

`pnmquantall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pnm path/to/input2.pnm ...</span>

- Save the quantised images to files named the same as the input files, but with the specified extension appended:

`pnmquantall -ext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pnm path/to/input2.pnm ...</span>
