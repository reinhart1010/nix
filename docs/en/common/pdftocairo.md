---
layout: page
title: common/pdftocairo (English)
description: "Converts PDF files to PNG/JPEG/TIFF/PDF/PS/EPS/SVG using cairo."
content_hash: 71e2901aca0a25e772216ac50887b2a63de88f8b
---
# pdftocairo

Converts PDF files to PNG/JPEG/TIFF/PDF/PS/EPS/SVG using cairo.
More information: <https://poppler.freedesktop.org>.

- Convert a PDF file to JPEG:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` -jpeg`

- Convert to PDF expanding the output to fill the paper:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>` -pdf -expand`

- Convert to SVG specifying the first/last page to convert:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.svg</span>` -svg -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_page</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">last_page</span>

- Convert to PNG with 200ppi resolution:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.png</span>` -png -r 200`

- Convert to grayscale TIFF setting paper size to A3:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` -tiff -gray -paper A3`

- Convert to PNG cropping x and y pixels from the top-left corner:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` -png -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_pixels</span>` -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_pixels</span>
