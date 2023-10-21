---
layout: page
title: linux/pstoedit (English)
description: "Convert PDF files into various image formats."
content_hash: d039b5819f4982fe689bbea05bf9d34b9752c7d3
last_modified_at: 2023-10-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pstoedit

Convert PDF files into various image formats.
More information: <http://www.pstoedit.net>.

- Convert a PDF page to PNG or JPEG format:

`pstoedit -page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page_number</span>` -f magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page.png|page.jpg]</span>

- Convert multiple PDF pages to numbered images:

`pstoedit -f magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page%d.png|page%d.jpg</span>
