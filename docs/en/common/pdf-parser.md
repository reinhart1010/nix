---
layout: page
title: common/pdf-parser (English)
description: "Identify fundamental elements of a PDF file without rendering it."
content_hash: e8afb49b81e96f20539ee243066e90f2e45d922e
---
# pdf-parser

Identify fundamental elements of a PDF file without rendering it.
More information: <https://blog.didierstevens.com/programs/pdf-tools>.

- Display statistics for a PDF file:

`pdf-parser --stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Display objects of type `/Font` in a PDF file:

`pdf-parser --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Font</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Search for strings in indirect objects:

`pdf-parser --search=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>
