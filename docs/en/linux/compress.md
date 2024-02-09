---
layout: page
title: linux/compress (English)
description: "Compress files using the Unix `compress` command."
content_hash: 7080bd0e73034100b0ec4d0f4e11c6aeecf018c2
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# compress

Compress files using the Unix `compress` command.
More information: <https://manned.org/compress.1>.

- Compress specific files:

`compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Compress specific files, ignore non-existent ones:

`compress -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Specify the maximum compression bits (9-16 bits):

`compress -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bits</span>

- Write to `stdout` (no files are changed):

`compress -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress files (functions like `uncompress`):

`compress -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display compression percentage:

`compress -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
