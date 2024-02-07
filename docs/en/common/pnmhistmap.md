---
layout: page
title: common/pnmhistmap (English)
description: "Draw a histogram of a PNM image."
content_hash: 08fa9d62011c3c1514515f956c9e54eaab32c7b1
last_modified_at: 2024-02-07
tldri18n_status: 2
---
# pnmhistmap

Draw a histogram of a PNM image.
More information: <https://netpbm.sourceforge.net/doc/pnmhistmap.html>.

- Draw a histogram of a PNM image:

`pnmhistmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Draw the histogram as dots instead of bars:

`pnmhistmap -dots `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Specify the range of intensity values to include:

`pnmhistmap -lval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minval</span>` -rval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maxval</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
