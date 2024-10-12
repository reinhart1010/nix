---
layout: page
title: linux/pdfdetach (English)
description: "List or extract attachments (embedded files) from a PDF file."
content_hash: d927475ba95a21151d225d65d5277ff77222d05b
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# pdfdetach

List or extract attachments (embedded files) from a PDF file.
See also: `pdfattach`, `pdfimages`, `pdfinfo`.
More information: <https://manned.org/pdfdetach>.

- List all attachments in a file with a specific text encoding:

`pdfdetach list -enc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>

- Save specific embedded file by specifying its number:

`pdfdetach -save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>

- Save specific embedded file by specifying its name:

`pdfdetach -savefile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>

- Save the embedded file with a custom output filename:

`pdfdetach -save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>

- Save the attachment from a file secured by owner/user password:

`pdfdetach -save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-opw|-upw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>
