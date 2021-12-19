---
layout: page
title: common/pdfposter (English)
description: "Convert a large-sheeted PDF into multiple A4 pages for printing."
content_hash: 8e6fbc404990b2c36807be9be5d80ec0cacb91e8
---
# pdfposter

Convert a large-sheeted PDF into multiple A4 pages for printing.
More information: <https://pdfposter.readthedocs.io>.

- Convert an A2 poster into 4 A4 pages:

`pdfposter --poster-size a2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file.pdf</span>

- Scale an A4 poster to A3 and then generate 2 A4 pages:

`pdfposter --scale 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file.pdf</span>
