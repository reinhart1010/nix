---
layout: page
title: common/pdfgrep (English)
description: "Search text in PDF files."
content_hash: cd7997dd4fc8ce0dc95e4c531836a2692a57dc1f
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/pdfgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdfgrep

Search text in PDF files.
More information: <https://pdfgrep.org>.

- Find lines that match pattern in a PDF:

`pdfgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>

- Include file name and page number for each matched line:

`pdfgrep --with-filename --page-number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>

- Do a case-insensitive search for lines that begin with "foo" and return the first 3 matches:

`pdfgrep --max-count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'^foo'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>

- Find pattern in files with a `.pdf` extension in the current directory recursively:

`pdfgrep --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Find pattern on files that match a specific glob in the current directory recursively:

`pdfgrep --recursive --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'*book.pdf'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>
