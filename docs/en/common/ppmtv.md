---
layout: page
title: common/ppmtv (English)
description: "Make a PPM Image look like taken from an American TV."
content_hash: 0f2a128a6d95f9bf315f9f584a3d035460d1690e
last_modified_at: 2023-10-31
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ppmtv

Make a PPM Image look like taken from an American TV.
Dim every other row of image data down by the specified dim factor (a number between 0 and 1).
More information: <https://netpbm.sourceforge.net/doc/ppmtv.html>.

- Give the PPM image an American TV appearance:

`ppmtv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dim_factor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Suppress all informational messages:

`ppmtv -quiet`

- Display version:

`ppmtv -version`
