---
layout: page
title: common/ppmfade (English)
description: "Generate a transition between two PPM images."
content_hash: e0b7373c0d56be6a46aeae55737c21e837b2d21c
last_modified_at: 2023-11-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ppmfade

Generate a transition between two PPM images.
More information: <https://netpbm.sourceforge.net/doc/ppmfade.html>.

- Generate a transition between two PPM images ([f]irst and [l]ast) using the specified effect:

`ppmfade -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.ppm</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.ppm</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mix|spread|shift|relief|oil|...</span>

- Generate a transition starting with the specified image and ending in a solid black image:

`ppmfade -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mix|spread|shift|relief|oil|...</span>

- Generate a transition starting with a solid black image and ending with the specified image:

`ppmfade -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mix|spread|shift|relief|oil|...</span>

- Store the resulting images in files named `base.NNNN.ppm` where `NNNN` is a increasing number:

`ppmfade -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.ppm</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.ppm</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mix|spread|shift|relief|oil|...</span>` -base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>
