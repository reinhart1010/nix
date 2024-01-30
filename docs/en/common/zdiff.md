---
layout: page
title: common/zdiff (English)
description: "Invoke `diff` on `gzip` archives."
content_hash: a5cc8c93be4c613cd52edc5cd827c423a92f9a81
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# zdiff

Invoke `diff` on `gzip` archives.
More information: <https://manned.org/zdiff>.

- Compare two files, uncompressing them if necessary:

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.gz</span>

- Compare a file to a `gzip` archive with the same name:

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
