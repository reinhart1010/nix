---
layout: page
title: common/pbzip2 (English)
description: "A parallel implementation of the `bzip2` file compressor."
content_hash: 4b231c228225bd51319c74d2cb320ab3c4c3e009
last_modified_at: 2024-01-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbzip2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbzip2

A parallel implementation of the `bzip2` file compressor.
See also: `bzip2`, `tar`.
More information: <https://manned.org/pbzip2>.

- Compress a file:

`pbzip2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file using the specified number of processors:

`pbzip2 -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- [d]ecompress a file:

`pbzip2 --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz2</span>

- Display help:

`pbzip2 -h`
