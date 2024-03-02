---
layout: page
title: common/ppmtoterm (English)
description: "Convert a PPM image to an ANSI ISO 6429 ASCII image."
content_hash: 5aae0fd1fe194f669404490422fbbd36674bb17f
last_modified_at: 2024-03-02
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtoterm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtoterm

Convert a PPM image to an ANSI ISO 6429 ASCII image.
See also: `ppmtoascii`, `pbmtoascii`, `pbmto4425`.
More information: <https://netpbm.sourceforge.net/doc/ppmtoterm.html>.

- Convert a PPM image to an ANSI ISO 6429 ASCII image, mapping each pixel to an individual character:

`ppmtoterm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.txt</span>
