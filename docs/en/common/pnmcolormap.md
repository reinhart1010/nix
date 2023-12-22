---
layout: page
title: common/pnmcolormap (English)
description: "Create quantization color map for a PNM image."
content_hash: 468f238017aa3c1f6039ccaff8afbd9efa09e264
last_modified_at: 2023-12-22
tldri18n_status: 2
---
# pnmcolormap

Create quantization color map for a PNM image.
More information: <https://netpbm.sourceforge.net/doc/pnmcolormap.html>.

- Generate an image using only `n_colors` or less colors as close as possible to the input image:

`pnmcolormap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Use the splitspread strategy for determining the output colors, possibly producing a better result for images with small details:

`pnmcolormap -splitspread `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Sort the resulting colormap, which is useful for comparing colormaps:

`pnmcolormap -sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
