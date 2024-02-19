---
layout: page
title: linux/id3v2 (English)
description: "Manages id3v2 tags, converts and lists id3v1."
content_hash: 4b98fb1f85f4deb2987cb71a7109a0a974b59883
last_modified_at: 2024-02-19
tldri18n_status: 2
---
# id3v2

Manages id3v2 tags, converts and lists id3v1.
More information: <https://manned.org/id3v2.1>.

- List all genres:

`id3v2 --list-genres`

- List all tags of specific files:

`id3v2 --list-tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Delete all `id3v2` or `id3v1` tags of specific files:

`id3v2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--delete-v2|--delete-v1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Display help:

`id3v2 --help`

- Display version:

`id3v2 --version`
