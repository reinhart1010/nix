---
layout: page
title: common/ppmtopcx (English)
description: "Convert a PPM image to a PCX file."
content_hash: ab607ef13a16decc527a8698d3a61be54de81c97
last_modified_at: 2023-11-10
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ppmtopcx

Convert a PPM image to a PCX file.
More information: <https://netpbm.sourceforge.net/doc/ppmtopcx.html>.

- Convert a PPM image to a PCX file:

`ppmtopcx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcx</span>

- Produce a PCX file with the specified color depth:

`ppmtopcx -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8bit|24bit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcx</span>
