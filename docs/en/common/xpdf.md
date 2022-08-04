---
layout: page
title: common/xpdf (English)
description: "Portable Document Format (PDF) file viewer."
content_hash: 54dbd97aa0c4bf22b1be8253349d5d4bce21c889
---
# xpdf

Portable Document Format (PDF) file viewer.
More information: <https://www.xpdfreader.com/xpdf-man.html>.

- Open a PDF file:

`xpdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Open a specific page in a PDF file:

`xpdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page_number</span>

- Open a compressed PDF file:

`xpdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf.tar</span>

- Open a PDF file in fullscreen mode:

`xpdf -fullscreen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Specify the initial zoom:

`xpdf -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75</span>`% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Specify the initial zoom at page width or full page:

`xpdf -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page|width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>
