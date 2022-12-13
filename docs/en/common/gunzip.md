---
layout: page
title: common/gunzip (English)
description: "Extract file(s) from a gzip (.gz) archive."
content_hash: d65e3ffa1b464a44028c014c072f6444661fd6b1
last_modified_at: 2022-12-13
---
# gunzip

Extract file(s) from a gzip (.gz) archive.
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
