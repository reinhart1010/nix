---
layout: page
title: common/pnmmercator (English)
description: "Perform Mercator transformations on Netpbm images."
content_hash: 00412600a64cbf52eeb8f13ed729c65d90b93f1a
last_modified_at: 2024-12-30
tldri18n_status: 2
---
# pnmmercator

Perform Mercator transformations on Netpbm images.
See also: `pnmglobe`.
More information: <https://netpbm.sourceforge.net/doc/pnmmercator.html>.

- Convert a rectangular projection worldmap to Mercator projection:

`pnmmercator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Convert a Mercator projection worldmap to rectangular projection:

`pnmmercator -inverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
