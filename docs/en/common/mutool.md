---
layout: page
title: common/mutool (English)
description: "Convert PDF files, query information and extract data."
content_hash: dafcf215726ce502950b4292888cf43c0fa5a127
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mutool

Convert PDF files, query information and extract data.
More information: <https://mupdf.readthedocs.io/en/latest/mupdf-command-line.html>.

- Convert pages 1-10 into 10 PNGs (Note: `%nd` in the output placeholder must be replaced with a print modifier like `%d` or `%2d`):

`mutool convert -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output%nd.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>

- Convert pages 2, 3 and 5 of a PDF into text in `stdout`:

`mutool draw -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,3,5</span>

- Concatenate multiple PDF files:

`mutool merge -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pdf path/to/input2.pdf ...</span>

- Query information about all content embedded in a PDF:

`mutool info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>

- Extract all images, fonts and resources embedded in a PDF out into the current directory:

`mutool extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>

- Print the outline (table of contents) of a PDF:

`mutool show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>` outline`
