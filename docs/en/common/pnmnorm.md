---
layout: page
title: common/pnmnorm (English)
description: "Normalize the contrast in a PNM image."
content_hash: a28c310bfab0f3a21173e7d2e1081e8effd58a1a
last_modified_at: 2024-02-10
tldri18n_status: 2
---
# pnmnorm

Normalize the contrast in a PNM image.
See also: `pnmhisteq`.
More information: <https://netpbm.sourceforge.net/doc/pnmnorm.html>.

- Force the brightest pixels to be white, the darkest pixels to be black and spread out the ones in between linearly:

`pnmnorm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Force the brightest pixels to be white, the darkest pixels to be black and spread out the ones in between quadratically such that pixels with a brightness of `n` become 50 % bright:

`pnmnorm -midvalue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Keep the pixels' hue, only modify the brightness:

`pnmnorm -keephues `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Specify a method to calculate a pixel's brightness:

`pnmnorm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">luminosity|colorvalue|saturation</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
