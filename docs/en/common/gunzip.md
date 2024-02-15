---
layout: page
title: common/gunzip (English)
description: "Extract files from a `gzip` (`.gz`) archive."
content_hash: 91a5b0ceeaa891602b4603e14f43181840742f53
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# gunzip

Extract files from a `gzip` (`.gz`) archive.
More information: <https://manned.org/gunzip>.

- Extract a file from an archive, replacing the original file if it exists:

`gunzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.gz</span>

- Extract a file to a target destination:

`gunzip --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.gz</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar</span>

- Extract a file and keep the archive file:

`gunzip --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.gz</span>

- List the contents of a compressed file:

`gunzip --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt.gz</span>

- Decompress an archive from `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.gz</span>` | gunzip`
