---
layout: page
title: common/ppmglobe (English)
description: "Generate strips of an image suitable to be glued onto a sphere."
content_hash: acc21a8e32638ecb1c043d5c4abcc89f84e4999d
last_modified_at: 2024-12-30
tldri18n_status: 2
---
# ppmglobe

Generate strips of an image suitable to be glued onto a sphere.
See also: `pnmmercator`.
More information: <https://netpbm.sourceforge.net/doc/ppmglobe.html>.

- Transform an image to strips that can be cut out and glues onto a sphere:

`ppmglobe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_strips</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Use the specified color for the areas between the strips:

`ppmglobe -background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_strips</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
