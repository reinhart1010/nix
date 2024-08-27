---
layout: page
title: linux/djxl (English)
description: "Decompress JPEG XL images."
content_hash: 9305e0345e58c98e839ce140b6963e986f10896f
last_modified_at: 2024-08-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/djxl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># djxl

Decompress JPEG XL images.
Accepted output extensions are PNG, APNG, JPEG, EXR, PGM, PPM, PNM, PFM, PAM, EXIF, XMP and JUMBF.
More information: <https://github.com/libjxl/libjxl>.

- Decompress a JPEG XL image to another format:

`djxl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jxl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ext</span>

- Display an extremely detailed help page:

`djxl --help --verbose --verbose --verbose --verbose`
