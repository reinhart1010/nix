---
layout: page
title: osx/stat (English)
description: "Display file status."
content_hash: 0658c5a1bbef37c0e544f88d6d473df6a3887b6b
last_modified_at: 2024-01-31
related_topics:
  - title: 中文 version
    url: /zh/osx/stat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stat

Display file status.
More information: <https://keith.github.io/xcode-man-pages/stat.1.html>.

- Show file properties such as size, permissions, creation and access dates among others:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Same as above but verbose (more similar to Linux's `stat`):

`stat -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show only octal file permissions:

`stat -f %Mp%Lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show owner and group of the file:

`stat -f "%Su %Sg" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show the size of the file in bytes:

`stat -f "%z %N" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
