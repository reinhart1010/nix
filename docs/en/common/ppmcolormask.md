---
layout: page
title: common/ppmcolormask (English)
description: "Produce a mask of areas of a certain color in a PPM image."
content_hash: ce4431534822337a73a594d929b88ec2b4dd6f81
last_modified_at: 2023-11-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ppmcolormask

Produce a mask of areas of a certain color in a PPM image.
More information: <https://netpbm.sourceforge.net/doc/ppmcolormask.html>.

- Produce a mask of areas of a certain color in the specified PPM image:

`ppmcolormask -color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red,blue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>
