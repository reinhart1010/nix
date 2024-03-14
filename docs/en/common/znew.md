---
layout: page
title: common/znew (English)
description: "Recompress files from `.Z` to gzip format."
content_hash: d5ae5e884a74e341bfe8ca5bc132564fcb04daec
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# znew

Recompress files from `.Z` to gzip format.
More information: <https://manned.org/znew>.

- Recompress a file from `.Z` to gzip format:

`znew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z</span>

- Recompress multiple files and display the achieved size reduction % per file:

`znew -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z path/to/file2.Z ...</span>

- Recompress a file using the slowest compression method (for optimal compression):

`znew -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z</span>

- Recompress a file, [K]eeping the `.Z` file if it is smaller than the gzip file:

`znew -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z</span>
