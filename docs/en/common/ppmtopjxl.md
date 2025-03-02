---
layout: page
title: common/ppmtopjxl (English)
description: "Convert a PPM image into an HP PaintJet XL PCL file."
content_hash: af86aa20cc513d8c70ebaf9b5a390e59454a4411
last_modified_at: 2024-12-29
tldri18n_status: 2
---
# ppmtopjxl

Convert a PPM image into an HP PaintJet XL PCL file.
More information: <https://netpbm.sourceforge.net/doc/ppmtopjxl.html>.

- Convert a PPM image into an PJXL file:

`ppmtopjxl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pjxl</span>

- Resize the input image:

`ppmtopjxl -xsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10cm</span>` -ysize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5cm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pjxl</span>

- Shift the input image:

`ppmtopjxl -xshift `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10pt</span>` -yshift `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5pt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pjxl</span>

- Do not use the normal TIFF 4.0 compression method:

`ppmtopjxl -nopack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pjxl</span>
