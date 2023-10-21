---
layout: page
title: linux/uncompress (English)
description: "Uncompress files compressed using the Unix `compress` command."
content_hash: d8f17e2c3546190acf456e64a185acdf3effb860
last_modified_at: 2023-10-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># uncompress

Uncompress files compressed using the Unix `compress` command.
More information: <https://manned.org/uncompress.1>.

- Uncompress specific files:

`uncompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z path/to/file2.Z ...</span>

- Uncompress specific files while ignoring non-existent ones:

`uncompress -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z path/to/file2.Z ...</span>

- Write to standard output (no files are changed and no `.Z` files are created):

`uncompress -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z path/to/file2.Z ...</span>

- Verbose mode (write to standard error about percentage reduction or expansion):

`uncompress -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z path/to/file2.Z ...</span>
