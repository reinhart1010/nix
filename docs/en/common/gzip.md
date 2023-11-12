---
layout: page
title: common/gzip (English)
description: "Compress/uncompress files with gzip compression (LZ77)."
content_hash: 7e412f80768a66f468b47aa7dc27eb7821d861b6
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/gzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gzip

Compress/uncompress files with gzip compression (LZ77).
More information: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Compress a file, replacing it with a gzipped compressed version:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Decompress a file, replacing it with the original uncompressed version:

`gzip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>`.gz`

- Compress a file, keeping the original file:

`gzip --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Compress a file specifying the output filename:

`gzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed_file.ext.gz</span>

- Decompress a gzipped file specifying the output filename:

`gzip -c -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>`.gz > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uncompressed_file.ext</span>

- Specify the compression level. 1=Fastest (Worst), 9=Slowest (Best), Default level is 6:

`gzip -9 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed_file.ext.gz</span>
