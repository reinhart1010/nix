---
layout: page
title: common/pdfimages (English)
description: "Utility for extracting images from PDFs."
content_hash: 9c019e8fb90d25cb2ae3161422402722dc237e2f
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/common/pdfimages.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdfimages

Utility for extracting images from PDFs.
More information: <https://manned.org/pdfimages>.

- Extract all images from a PDF file and save them as PNGs:

`pdfimages -png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename_prefix</span>

- Extract images from pages 3 to 5:

`pdfimages -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename_prefix</span>

- Extract images from a PDF file and include the page number in the output filenames:

`pdfimages -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename_prefix</span>

- List information about all the images in a PDF file:

`pdfimages -list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>
