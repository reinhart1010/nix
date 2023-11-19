---
layout: page
title: common/ppmshift (English)
description: "Shift the lines in a PPM image by a randomized amount."
content_hash: 00dc22fd5bae3e47f055e2427687a6998a560c34
last_modified_at: 2023-11-19
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmshift.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmshift

Shift the lines in a PPM image by a randomized amount.
More information: <https://netpbm.sourceforge.net/doc/ppmshift.html>.

- Shift the lines in the input image by a randomized amount not exceeding s to the left or to the right:

`ppmshift `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>
