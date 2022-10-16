---
layout: page
title: common/ouch (English)
description: "Command-line utility for compressing and decompressing files and directories."
content_hash: ef135f4e4f26cf408ecb6013a281cd692f809b7d
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ouch

Command-line utility for compressing and decompressing files and directories.
More information: <https://crates.io/crates/ouch>.

- Decompress a specific file:

`ouch decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.tar.xz</span>

- Decompress a file to a specific location:

`ouch decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.tar.xz</span>` --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Decompress multiple files:

`ouch decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive1.tar path/to/archive2.tar.gz ...</span>

- Compress files:

`ouch compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>
