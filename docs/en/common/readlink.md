---
layout: page
title: common/readlink (English)
description: "Follow symlinks and get symlink information."
content_hash: e887b3df7c609ff6ba26d39ce323c46debf69ed1
last_modified_at: 2022-12-06
related_topics:
  - title: italiano version
    url: /it/common/readlink.html
    icon: bi bi-globe
---
# readlink

Follow symlinks and get symlink information.
More information: <https://www.gnu.org/software/coreutils/readlink>.

- Get the actual file to which the symlink points:

`readlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Get the absolute path to a file:

`readlink -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
