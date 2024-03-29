---
layout: page
title: common/ppmpat (English)
description: "Produce a PPM image with a pattern."
content_hash: 9fb830e5d7576d90656c81b957ce2464eeb57b3e
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ppmpat

Produce a PPM image with a pattern.
More information: <https://netpbm.sourceforge.net/doc/ppmpat.html>.

- Produce a PPM file of the specified pattern with the specified dimensions:

`ppmpat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gingham2|gingham3|madras|tartan|poles|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>

- Produce a PPM file of a camo pattern using the specified colors:

`ppmpat -camo -color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color1,color2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>
