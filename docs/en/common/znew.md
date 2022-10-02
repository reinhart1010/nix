---
layout: page
title: common/znew (English)
description: "Recompress files from `.Z` to `.gz` format."
content_hash: db89b1fa8e22a01dfe93d6b9ba5feb7614122522
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># znew

Recompress files from `.Z` to `.gz` format.
More information: <https://manned.org/znew>.

- Recompress a file from `.Z` to `.gz` format:

`znew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z</span>

- Recompress multiple files and display the achieved size reduction % per file:

`znew -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.Z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file3.Z</span>

- Recompress a file using the slowest compression method (for optimal compression):

`znew -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z</span>

- Recompress a file, [K]eeping the `.Z` file if it is smaller than the `.gz` file:

`znew -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z</span>
