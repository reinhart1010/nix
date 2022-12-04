---
layout: page
title: osx/stat (English)
description: "Display file status."
content_hash: 497b87b1e2755b41eaf93cba23a8117f428383d8
last_modified_at: 2022-12-04
related_topics:
  - title: 中文 version
    url: /zh/osx/stat.html
    icon: bi bi-globe
---
# stat

Display file status.
More information: <https://ss64.com/osx/stat.html>.

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
