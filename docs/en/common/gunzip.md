---
layout: page
title: common/gunzip (English)
description: "Extract file(s) from a `gzip` (`.gz`) archive."
content_hash: 48d15984fc56a87fe77337793c238a756b1fad13
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# gunzip

Extract file(s) from a `gzip` (`.gz`) archive.
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
