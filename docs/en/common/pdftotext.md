---
layout: page
title: common/pdftotext (English)
description: "Convert PDF files to plain text format."
content_hash: c24fb942a5c3d2947081344728e813669fee6c5c
last_modified_at: 2023-08-09
related_topics:
  - title: Deutsch version
    url: /de/common/pdftotext.html
    icon: bi bi-globe
---
# pdftotext

Convert PDF files to plain text format.
More information: <https://www.xpdfreader.com/pdftotext-man.html>.

- Convert `filename.pdf` to plain text and print it to `stdout`:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pdf</span>` -`

- Convert `filename.pdf` to plain text and save it as `filename.txt`:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pdf</span>

- Convert `filename.pdf` to plain text and preserve the layout:

`pdftotext -layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pdf</span>

- Convert `input.pdf` to plain text and save it as `output.txt`:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.txt</span>

- Convert pages 2, 3 and 4 of `input.pdf` to plain text and save them as `output.txt`:

`pdftotext -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.txt</span>
