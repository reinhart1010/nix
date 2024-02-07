---
layout: page
title: common/pnmcrop (English)
description: "Crop PNM images."
content_hash: df2204d3b105e747cf040b82017df1ec6ce5c3c0
last_modified_at: 2024-02-07
tldri18n_status: 2
---
# pnmcrop

Crop PNM images.
More information: <https://netpbm.sourceforge.net/doc/pnmcrop.html>.

- Remove white borders on a PNM image:

`pnmcrop -white `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Remove borders of the specified color that are on the top and left side of the image:

`pnmcrop -bg-color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>` -top -left `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Determine the color of the borders to be removed by the color of the pixel in the specified corner:

`pnmcrop -bg-corner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topleft|topright|bottomleft|bottomright</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Leave a border with a width of `n` pixels. Additionally, specify the behaviour if the image is entirely made out of background:

`pnmcrop -margins `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -blank-image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pass|minimize|maxcrop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
