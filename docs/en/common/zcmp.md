---
layout: page
title: common/zcmp (English)
description: "Compare compressed files."
content_hash: 9c03a8f546e12724831e68b8bd19ca15a68c5242
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# zcmp

Compare compressed files.
More information: <https://manned.org/zcmp>.

- Invoke `cmp` on two files compressed via `gzip`:

`zcmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.gz</span>

- Compare a file to its gzipped version (assuming `.gz` exists already):

`zcmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
