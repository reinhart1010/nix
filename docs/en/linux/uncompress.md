---
layout: page
title: linux/uncompress (English)
description: "Uncompress files compressed using the Unix `compress` command."
content_hash: 69561e0af682e9015c544504cc92b78658aaed13
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# uncompress

Uncompress files compressed using the Unix `compress` command.
More information: <https://manned.org/uncompress.1>.

- Uncompress specific files:

`uncompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z path/to/file2.Z ...</span>

- Uncompress specific files while ignoring non-existent ones:

`uncompress -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z path/to/file2.Z ...</span>

- Write to `stdout` (no files are changed and no `.Z` files are created):

`uncompress -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z path/to/file2.Z ...</span>

- Verbose mode (write to `stderr` about percentage reduction or expansion):

`uncompress -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.Z path/to/file2.Z ...</span>
