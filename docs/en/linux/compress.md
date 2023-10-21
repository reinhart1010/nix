---
layout: page
title: linux/compress (English)
description: "Compress files using the Unix `compress` command."
content_hash: 7f9a76fb10db490e26c824be3da4239d3dcc0675
last_modified_at: 2023-10-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># compress

Compress files using the Unix `compress` command.
More information: <https://manned.org/compress.1>.

- Compress specific files:

`compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Compress specific files, ignore non-existent ones:

`compress -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Set maximum compression bits (9-16 bits):

`compress -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bits</span>

- Write to standard output (no files are changed):

`compress -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress files (functions like `uncompress`):

`compress -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display compression percentage:

`compress -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
