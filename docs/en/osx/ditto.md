---
layout: page
title: osx/ditto (English)
description: "Copy files and directories."
content_hash: 86522358d8dfda4ccd40013f677e58a4e70090fd
last_modified_at: 2024-01-31
related_topics:
  - title: বাংলা version
    url: /bn/osx/ditto.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/ditto.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/ditto.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ditto

Copy files and directories.
More information: <https://keith.github.io/xcode-man-pages/ditto.1.html>.

- Overwrite contents of destination directory with contents of source directory:

`ditto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_directory</span>

- Print a line to the Terminal window for every file that's being copied:

`ditto -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_directory</span>

- Copy a given file or directory, while retaining the original file permissions:

`ditto -rsrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_directory</span>
