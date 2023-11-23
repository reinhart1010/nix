---
layout: page
title: common/ppmrainbow (English)
description: "Generate a rainbow."
content_hash: a24cba42c8f9efd6b1441e2000543f23f056c8fa
last_modified_at: 2023-11-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmrainbow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmrainbow

Generate a rainbow.
More information: <https://netpbm.sourceforge.net/doc/ppmrainbow.html>.

- Generate a rainbow consisting of the specified colors:

`ppmrainbow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color1 color2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>

- Specify the size of the output in pixels:

`ppmrainbow -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color1 color2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>

- End the rainbow with the last color specified, do not repeat the first color:

`ppmrainbow -norepeat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color1 color2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>
