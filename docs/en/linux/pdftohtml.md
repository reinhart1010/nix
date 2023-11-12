---
layout: page
title: linux/pdftohtml (English)
description: "Convert PDF files into HTML, XML and PNG images."
content_hash: 33b5ebcc1e82d04074c233e801297f88475db463
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pdftohtml

Convert PDF files into HTML, XML and PNG images.
More information: <https://manned.org/pdftohtml>.

- Convert a PDF file to an HTML file:

`pdftohtml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.html</span>

- Ignore images in the PDF file:

`pdftohtml -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.html</span>

- Generate a single HTML file that includes all PDF pages:

`pdftohtml -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.html</span>

- Convert a PDF file to an XML file:

`pdftohtml -xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xml</span>
