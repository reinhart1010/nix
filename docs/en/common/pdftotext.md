---
layout: page
title: common/pdftotext (English)
description: "Convert PDF files to plain text format."
content_hash: dc7c10053268e0e2205e376a840bc6a17e4b3e17
---
# pdftotext

Convert PDF files to plain text format.
More information: <https://www.xpdfreader.com/pdftotext-man.html>.

- Convert `filename.pdf` to plain text and print it to standard output:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pdf</span>` -`

- Convert `filename.pdf` to plain text and save it as `filename.txt`:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pdf</span>

- Convert `filename.pdf` to plain text and preserve the layout:

`pdftotext -layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pdf</span>

- Convert `input.pdf` to plain text and save it as `output.txt`:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.txt</span>

- Convert pages 2, 3 and 4 of `input.pdf` to plain text and save them as `output.txt`:

`pdftotext -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.txt</span>
