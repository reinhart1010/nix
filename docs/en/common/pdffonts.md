---
layout: page
title: common/pdffonts (English)
description: "Portable Document Format (PDF) file fonts information viewer."
content_hash: 56fbe73390f981b297e0c28079195bf36659b558
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pdffonts

Portable Document Format (PDF) file fonts information viewer.
More information: <https://www.xpdfreader.com/pdffonts-man.html>.

- Print PDF file fonts information:

`pdffonts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Specify user password for PDF file to bypass security restrictions:

`pdffonts -upw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Specify owner password for PDF file to bypass security restrictions:

`pdffonts -opw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Print additional information on location of the font that will be used when the PDF file is rasterized:

`pdffonts -loc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Print additional information on location of the font that will be used when the PDF file is converted to PostScript:

`pdffonts -locPS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>
