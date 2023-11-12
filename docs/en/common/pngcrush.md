---
layout: page
title: common/pngcrush (English)
description: "PNG compression utility."
content_hash: 2a260ce080655406bf981d668e05cfd9e7df6ed5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pngcrush

PNG compression utility.
More information: <https://pmt.sourceforge.io/pngcrush>.

- Compress a PNG file:

`pngcrush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">in.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out.png</span>

- Compress all PNGs and output them to the specified directory:

`pngcrush -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>` *.png`

- Compress PNG file with all 114 available algorithms and pick the best result:

`pngcrush -rem allb -brute -reduce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">in.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out.png</span>
