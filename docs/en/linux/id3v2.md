---
layout: page
title: linux/id3v2 (English)
description: "Manages id3v2 tags, converts and lists id3v1."
content_hash: 1df61fdee20a8f31e8478150f358e248b38e26af
last_modified_at: 2022-12-23
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># id3v2

Manages id3v2 tags, converts and lists id3v1.
More information: <https://manned.org/id3v2.1>.

- List all genres:

`id3v2 ‐‐list‐genres`

- List all tags of specific files:

`id3v2 --list-tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Delete all `id3v2` or `id3v1` tags of specific files:

`id3v2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--delete‐v2|--delete‐v1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Display help:

`id3v2 --help`

- Display version:

`id3v2 ‐‐version`
