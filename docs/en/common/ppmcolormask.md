---
layout: page
title: common/ppmcolormask (English)
description: "Produce a mask of areas of a certain color in a PPM image."
content_hash: ce4431534822337a73a594d929b88ec2b4dd6f81
last_modified_at: 2023-11-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmcolormask.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmcolormask

Produce a mask of areas of a certain color in a PPM image.
More information: <https://netpbm.sourceforge.net/doc/ppmcolormask.html>.

- Produce a mask of areas of a certain color in the specified PPM image:

`ppmcolormask -color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red,blue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>
