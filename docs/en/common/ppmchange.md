---
layout: page
title: common/ppmchange (English)
description: "Change all pixels of one color in a PPM image to another color."
content_hash: a8e5f8dec1e41c86985b1c5041a062f578329262
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ppmchange

Change all pixels of one color in a PPM image to another color.
More information: <https://netpbm.sourceforge.net/doc/ppmchange.html>.

- Exchange the first color in each `oldcolor` - `newcolor` pair with the second color:

`ppmchange `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oldcolor1 newcolor1 oldcolor2 newcolor2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Specify how similar colors must be in order to be considered the same:

`ppmchange -closeness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percentage</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oldcolor1 newcolor1 oldcolor2 newcolor2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Replace all pixels not specified in the arguments by a color:

`ppmchange -remainder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oldcolor1 newcolor1 oldcolor2 newcolor2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
