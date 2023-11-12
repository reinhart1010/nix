---
layout: page
title: linux/mksquashfs (English)
description: "Create or append files and directories to squashfs filesystems."
content_hash: 8fbdd379cafe1d27b35692031251902fd256838b
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/mksquashfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mksquashfs

Create or append files and directories to squashfs filesystems.
More information: <https://manned.org/mksquashfs>.

- Create or append files and directories to a squashfs filesystem (compressed using `gzip` by default):

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>

- Create or append files and directories to a squashfs filesystem, using a specific [comp]ression algorithm:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>` -comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gzip|lzo|lz4|xz|zstd|lzma</span>

- Create or append files and directories to a squashfs filesystem, [e]xcluding some of them:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file|directory1 file|directory2 ...</span>

- Create or append files and directories to a squashfs filesystem, [e]xcluding those ending with `.gz`:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>` -wildcards -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.gz</span>`"`

- Create or append files and directories to a squashfs filesystem, [e]xcluding those matching a regular expression:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>` -regex -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`"`
