---
layout: page
title: common/pdfinfo (English)
description: "Portable Document Format (PDF) file information viewer."
content_hash: d192491f0075a19c48c2b4706f49d5b947a2d25e
---
# pdfinfo

Portable Document Format (PDF) file information viewer.
More information: <https://www.xpdfreader.com/pdfinfo-man.html>.

- Print PDF file information:

`pdfinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Specify user password for PDF file to bypass security restrictions:

`pdfinfo -upw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Specify owner password for PDF file to bypass security restrictions:

`pdfinfo -opw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>
