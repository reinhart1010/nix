---
layout: page
title: common/pigz (English)
description: "Multithreaded zlib compression utility."
content_hash: 3d2ec07f9e2540289a45987481f724943258cddd
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# pigz

Multithreaded zlib compression utility.
More information: <https://github.com/madler/pigz>.

- Compress a file with default options:

`pigz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file using the best compression method:

`pigz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file using no compression and 4 processors:

`pigz -0 -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a directory using tar:

`tar cf - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` | pigz > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tar.gz</span>

- Decompress a file:

`pigz -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.gz</span>

- List the contents of an archive:

`pigz -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.gz</span>
