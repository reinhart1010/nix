---
layout: page
title: linux/sqfstar (English)
description: "Create a squashfs filesystem from a tar archive."
content_hash: 554e48649951e8074b1a225b4e72cafa570d0e15
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/sqfstar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sqfstar

Create a squashfs filesystem from a tar archive.
More information: <https://manned.org/sqfstar>.

- Create a squashfs filesystem (compressed using `gzip` by default) from an uncompressed tar archive:

`sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar</span>

- Create a squashfs filesystem from a tar archive compressed with `gzip`, and [comp]ress the filesystem using a specific algorithm:

`zcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.gz</span>` | sqfstar -comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gzip|lzo|lz4|xz|zstd|lzma</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>

- Create a squashfs filesystem from a tar archive compressed with `xz`, excluding some of the files:

`xzcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.xz</span>` | sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Create a squashfs filesystem from a tar archive compressed with `zstd`, excluding files ending with `.gz`:

`zstdcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.zst</span>` | sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.gz</span>`"`

- Create a squashfs filesystem from a tar archive compressed with `lz4`, excluding files matching a regular expression:

`lz4cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.lz4</span>` | sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>` -regex "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`"`
