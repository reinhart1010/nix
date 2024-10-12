---
layout: page
title: linux/pdfattach (English)
description: "Add a new attachment (embedded file) to an existing PDF file."
content_hash: ad1632952d32521d69130337759fc94a51874197
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# pdfattach

Add a new attachment (embedded file) to an existing PDF file.
See also: `pdfdetach`, `pdfimages`, `pdfinfo`.
More information: <https://manned.org/pdfattach>.

- Add a new attachment to an existing PDF file:

`pdfattach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_to_attach</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>

- Replace attachment with same name if it exists:

`pdfattach -replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_to_attach</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>

- Display help:

`pdfattach -h`

- Display version:

`pdfattach -v`
