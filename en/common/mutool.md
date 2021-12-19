---
layout: page
title: common/mutool (English)
description: "Convert PDF files, query information and extract data."
content_hash: 8bb025780bcc785829fa2daff0daaa2d131f13f7
---
# mutool

Convert PDF files, query information and extract data.
More information: <https://mupdf.com/docs>.

- Convert pages 1-10 into 10 PNGs:

`mutool convert -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image%d.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>

- Convert pages 2, 3 and 5 of a PDF into text in the standard output:

`mutool draw -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,3,5</span>

- Concatenate two PDFs:

`mutool merge -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input1.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.pdf</span>

- Query information about all content embedded in a PDF:

`mutool info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>

- Extract all images, fonts and resources embedded in a PDF out into the current directory:

`mutool extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>

- Print the outline (table of contents) of a PDF:

`mutool show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` outline`
