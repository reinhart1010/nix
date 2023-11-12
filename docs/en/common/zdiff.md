---
layout: page
title: common/zdiff (English)
description: "Invoke `diff` on gzipped files."
content_hash: 2e7b88410edf180eec401fed85518d03041c823d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# zdiff

Invoke `diff` on gzipped files.
More information: <https://manned.org/zdiff>.

- Compare two files, uncompressing them if necessary:

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.gz</span>

- Compare a file to a gzipped archive with the same name:

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
