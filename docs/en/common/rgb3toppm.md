---
layout: page
title: common/rgb3toppm (English)
description: "Combine three PGM images into one PPM image."
content_hash: 10e75e7df4643455e0984fab17d46baf625f77de
last_modified_at: 2024-12-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rgb3toppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rgb3toppm

Combine three PGM images into one PPM image.
See also: `ppmtorgb3`.
More information: <https://netpbm.sourceforge.net/doc/rgb3toppm.html>.

- Combine three PGM images (representing red, green and blue color components) into one PPM image:

`rgb3toppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/red_file.ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/green_file.ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/blue_file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
