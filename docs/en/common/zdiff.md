---
layout: page
title: common/zdiff (English)
description: "Invoke `diff` on gzipped files."
content_hash: 2e7b88410edf180eec401fed85518d03041c823d
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zdiff

Invoke `diff` on gzipped files.
More information: <https://manned.org/zdiff>.

- Compare two files, uncompressing them if necessary:

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.gz</span>

- Compare a file to a gzipped archive with the same name:

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
