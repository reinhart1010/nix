---
layout: page
title: common/mutool (English)
description: "Convert, query information and extract data from PDF files."
content_hash: 048d44e36019fa1c23271efaae9f8ccc9ef5f070
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# mutool

Convert, query information and extract data from PDF files.
More information: <https://mupdf.readthedocs.io/en/latest/mupdf-command-line.html>.

- Convert a range of pages to PNGs (Note: `%nd` in the output placeholder must be replaced with a print modifier like `%d` or `%2d`):

`mutool convert -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output%nd.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>

- Convert one or more pages of a PDF into text in `stdout`:

`mutool draw -F txt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,3,5,...</span>

- Concatenate multiple PDF files:

`mutool merge -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pdf path/to/input2.pdf ...</span>

- Query information about all content embedded in a PDF:

`mutool info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>

- Extract all images, fonts and resources embedded in a PDF to the current directory:

`mutool extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>

- Show the outline (table of contents) of a PDF:

`mutool show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>` outline`
