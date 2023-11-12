---
layout: page
title: linux/compress (English)
description: "Compress files using the Unix `compress` command."
content_hash: 6da176ac8ecd7fedc885fd8c8982900a1ef80b61
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# compress

Compress files using the Unix `compress` command.
More information: <https://manned.org/compress.1>.

- Compress specific files:

`compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Compress specific files, ignore non-existent ones:

`compress -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Set maximum compression bits (9-16 bits):

`compress -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bits</span>

- Write to `stdout` (no files are changed):

`compress -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress files (functions like `uncompress`):

`compress -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display compression percentage:

`compress -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
