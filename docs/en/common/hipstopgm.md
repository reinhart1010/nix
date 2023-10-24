---
layout: page
title: common/hipstopgm (English)
description: "Read a HIPS file as input and return a PGM image as output."
content_hash: 57c6f483e67e63e1b86b07f9cdbc78235bc4c735
last_modified_at: 2023-10-24
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hipstopgm

Read a HIPS file as input and return a PGM image as output.
If the HIPS file contains more than one frame in sequence, `hipstopgm` will concatenate all the frames vertically.
More information: <https://netpbm.sourceforge.net/doc/hipstopgm.html>.

- Convert a HIPS file into a PGM image:

`hipstopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.hips</span>

- Suppress all informational messages:

`hipstopgm -quiet`

- Display version:

`hipstopgm -version`
