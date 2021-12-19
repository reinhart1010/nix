---
layout: page
title: common/rmdir (English)
description: "Removes a directory."
content_hash: 8f3fd77e5fa6a3f8d8d5dacb565ab3de850d18e1
related_topics:
  - title: தமிழ் version
    url: /ta/common/rmdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rmdir.html
    icon: bi bi-globe
---
# rmdir

Removes a directory.
More information: <https://www.gnu.org/software/coreutils/rmdir>.

- Remove directory, provided it is empty. Use `rm -r` to remove non-empty directories:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Remove the target and its parent directories (useful for nested dirs):

`rmdir -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
