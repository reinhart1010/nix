---
layout: page
title: common/gzip (English)
description: "Compress/uncompress files with `gzip` compression (LZ77)."
content_hash: b825d6f86d87738bf4941a84bcc324a31403e933
last_modified_at: 2024-06-05
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/gzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gzip

Compress/uncompress files with `gzip` compression (LZ77).
More information: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Compress a file, replacing it with a `gzip` archive:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress a file, replacing it with the original uncompressed version:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress path/to/file.gz</span>

- Compress a file, keeping the original file:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-k|--keep path/to/file</span>

- Compress a file, specifying the output filename:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout path/to/file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.gz</span>

- Decompress a `gzip` archive specifying the output filename:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.gz</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/uncompressed_file</span>

- Specify the compression level. 1 is the fastest (low compression), 9 is the slowest (high compression), 6 is the default:

`gzip -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.gz</span>

- Display the name and reduction percentage for each file compressed or decompressed:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.gz</span>
