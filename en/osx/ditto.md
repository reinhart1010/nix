---
layout: page
title: osx/ditto (English)
description: "Copy files and directories."
content_hash: 9df8c5790d07447b13812ae7940f0c6ea4ef6dd7
related_topics:
  - title: বাংলা version
    url: /bn/osx/ditto.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/ditto.html
    icon: bi bi-globe
---
# ditto

Copy files and directories.
More information: <https://ss64.com/osx/ditto.html>.

- Overwrite contents of destination directory with contents of source directory:

`ditto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Print a line to the Terminal window for every file that's being copied:

`ditto -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Copy a given file or directory, while retaining the original file permissions:

`ditto -rsrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>
