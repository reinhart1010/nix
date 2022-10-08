---
layout: page
title: common/lzip (English)
description: "Lzip is a lossless data compressor with a user interface similar to `gzip` or `bzip2`."
content_hash: 47d59e3b54b60f670e0f9fcff14040707f39625e
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lzip

Lzip is a lossless data compressor with a user interface similar to `gzip` or `bzip2`.
Lzip uses a simplified form of the "Lempel-Ziv-Markovchain-Algorithm"z (LZMA) stream format and provides a 3 factor integrity checking to maximize interoperability and optimize safety.
More information: <https://www.nongnu.org/lzip>.

- Archive a file, replacing it with with a compressed version:

`lzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Archive a file, keeping the input file:

`lzip -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Archive a file with the best compression (level=9):

`lzip -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --best`

- Archive a file at the fastest speed (level=0):

`lzip -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --fast`

- Test the integrity of compressed file:

`lzip --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.lz</span>

- Decompress a file, replacing it with the original uncompressed version:

`lzip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.lz</span>

- Decompress a file, keeping the archive:

`lzip -d -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.lz</span>

- List files which are in an archive and show compression stats:

`lzip --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.lz</span>
