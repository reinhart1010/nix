---
layout: page
title: common/wkhtmltopdf (English)
description: "An open-source command-line tool to convert HTML documents or web pages into PDF files."
content_hash: 084fcca54e5b075b0b8d15ed10a42231f77f74bf
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wkhtmltopdf

An open-source command-line tool to convert HTML documents or web pages into PDF files.
More information: <https://wkhtmltopdf.org/>.

- Convert a HTML document into PDF:

`wkhtmltopdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>

- Specify the PDF page size (please see `PaperSize` of `QPrinter` for supported sizes):

`wkhtmltopdf --page-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>

- Set the PDF page margins:

`wkhtmltopdf --margin-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top|bottom|left|right</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10mm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>

- Set the PDF page orientation:

`wkhtmltopdf --orientation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Landscape|Portrait</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>

- Generate a greyscale version of the PDF document:

`wkhtmltopdf --grayscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>
