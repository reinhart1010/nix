---
layout: page
title: common/xzcmp (English)
description: "Invokes `cmp` on files compressed with `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd`."
content_hash: edeb8ce8e82bd6318e1d91410e468c589aa97d0b
last_modified_at: 2023-07-16
---
# xzcmp

Invokes `cmp` on files compressed with `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd`.
All options specified are passed directly to `cmp`.
More information: <https://manned.org/xzcmp>.

- Compare two specific files:

`xzcmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
