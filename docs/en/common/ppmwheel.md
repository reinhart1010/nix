---
layout: page
title: common/ppmwheel (English)
description: "Generate a PPM image of a color wheel."
content_hash: 4d8a177ba9a8bf02ad8b96974b5ba737b5877402
last_modified_at: 2024-12-29
tldri18n_status: 2
---
# ppmwheel

Generate a PPM image of a color wheel.
More information: <https://netpbm.sourceforge.net/doc/ppmwheel.html>.

- Generate a color wheel of type `Ppmcirc`:

`ppmwheel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diameter</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Generate a color wheel of type `Hue-value`:

`ppmwheel -huevalue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diameter</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Generate a color wheel of type `Hue-saturation`:

`ppmwheel -huesaturation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diameter</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
