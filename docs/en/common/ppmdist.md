---
layout: page
title: common/ppmdist (English)
description: "Produce a grayscale version of a PPM image."
content_hash: 0d1429a718b184229314ab86aed37a43a1ee4dcd
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ppmdist

Produce a grayscale version of a PPM image.
More information: <https://netpbm.sourceforge.net/doc/ppmdist.html>.

- Produce a grayscale version of the specified PPM image:

`ppmdist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>

- Specify the method used to map colors to graylevels:

`ppmdist -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequency|intensity</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>
