---
layout: page
title: common/xzdiff (English)
description: "Invokes `diff` on files compressed with `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd`."
content_hash: f5e111e49479bb162a337b3fc5134b17e9747aad
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# xzdiff

Invokes `diff` on files compressed with `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd`.
All options specified are passed directly to `diff`.
More information: <https://manned.org/xzdiff>.

- Compare two files:

`xzdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Compare two files, showing the differences side by side:

`xzdiff --side-by-side `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Compare two files and report only that they differ (no details on what is different):

`xzdiff --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Compare two files and report when the files are the same:

`xzdiff --report-identical-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Compare two files using paginated results:

`xzdiff --paginate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
