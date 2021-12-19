---
layout: page
title: osx/stat (English)
description: "Display file status."
content_hash: 7a9570c08ce8c637b9d393a74e740409851f6422
related_topics:
  - title: 中文 version
    url: /zh/osx/stat.html
    icon: bi bi-globe
---
# stat

Display file status.
More information: <https://ss64.com/osx/stat.html>.

- Show file properties such as size, permissions, creation and access dates among others:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Same as above but verbose (more similar to Linux's `stat`):

`stat -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Show only octal file permissions:

`stat -f %Mp%Lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Show owner and group of the file:

`stat -f "%Su %Sg" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Show the size of the file in bytes:

`stat -f "%z %N" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
