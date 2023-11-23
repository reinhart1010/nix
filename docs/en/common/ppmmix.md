---
layout: page
title: common/ppmmix (English)
description: "Blend together two PPM images."
content_hash: e7ad1aedca0dcb04ae74e9232089ff0393fcee71
last_modified_at: 2023-11-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmmix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmmix

Blend together two PPM images.
More information: <https://netpbm.sourceforge.net/doc/ppmmix.html>.

- Blend the specified PPM images using fadefactor to control the weight of each image:

`ppmmix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fadefactor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file1.ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file2.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>
