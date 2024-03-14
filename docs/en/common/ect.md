---
layout: page
title: common/ect (English)
description: "Efficient Compression Tool."
content_hash: 6ebce245f25a27b3a8edb66e0c15263c524b158b
last_modified_at: 2024-03-14
related_topics:
  - title: italiano version
    url: /it/common/ect.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ect

Efficient Compression Tool.
File optimizer written in C++. It supports PNG, JPEG, gzip and Zip files.
More information: <https://github.com/fhanau/Efficient-Compression-Tool>.

- Compress a file:

`ect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a file with specified compression level and multithreading (1=Fastest (Worst), 9=Slowest (Best), default is 3):

`ect -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` --mt-deflate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Compress all files in a directory recursively:

`ect -recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Compress a file, keeping the original modification time:

`ect -keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a file, stripping metadata:

`ect -strip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>
