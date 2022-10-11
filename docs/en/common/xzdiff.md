---
layout: page
title: common/xzdiff (English)
description: "Invokes the diff command on files compressed with xz, lzma, gzip, bzip2, lzop, or zstd."
content_hash: 66fa05531526701eca1f05ba9d3c82c10782d9ff
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xzdiff

Invokes the diff command on files compressed with xz, lzma, gzip, bzip2, lzop, or zstd.
All options specified are passed directly to diff.
More information: <https://manned.org/xzdiff>.

- Compare files:

`xzdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Compare files, showing the differences side by side:

`xzdiff --side-by-side `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Compare files and report only that they differ (no details on what is different):

`xzdiff --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Compare files and report when the files are the same:

`xzdiff --report-identical-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Compare files using paginated results:

`xzdiff --paginate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Compare directories recursively (shows names for differing files/directories as well as changes made to files):

`diff --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
