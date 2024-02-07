---
layout: page
title: common/pnmhisteq (English)
description: "Histogram-equalize a PNM image."
content_hash: db8381a665bc9d422d4d121e474dd0120390f3b9
last_modified_at: 2024-02-07
tldri18n_status: 2
---
# pnmhisteq

Histogram-equalize a PNM image.
More information: <https://netpbm.sourceforge.net/doc/pnmhisteq.html>.

- Increase the contrast of a PNM image using histogram equalization:

`pnmhisteq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Only modify grey pixels:

`pnmhisteq -grey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Do not include black or white pixels in the histogram equalization:

`pnmhisteq -no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">black|white</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
