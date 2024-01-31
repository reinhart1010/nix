---
layout: page
title: common/znew (English)
description: "Recompress files from `.Z` to `.gz` format."
content_hash: 93fecec5507ad8f5d9879c14d9affeacbb52ba43
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# znew

Recompress files from `.Z` to `.gz` format.
More information: <https://manned.org/znew>.

- Recompress a file from `.Z` to `.gz` format:

`znew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z</span>

- Recompress multiple files and display the achieved size reduction % per file:

`znew -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z path/to/file2.Z ...</span>

- Recompress a file using the slowest compression method (for optimal compression):

`znew -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z</span>

- Recompress a file, [K]eeping the `.Z` file if it is smaller than the `.gz` file:

`znew -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z</span>
