---
layout: page
title: common/ptargrep (English)
description: "Find regular expression patterns in tar archive files."
content_hash: 53e299159002306342f9e1ba00dffa9b5116f237
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# ptargrep

Find regular expression patterns in tar archive files.
More information: <https://manned.org/ptargrep>.

- Search for a pattern within one or more `tar` archives:

`ptargrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Extract to the current directory using the basename of the file from the archive:

`ptargrep --basename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for a case-insensitive pattern matching within a `tar` archive:

`ptargrep --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
