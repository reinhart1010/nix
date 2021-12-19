---
layout: page
title: common/atq (English)
description: "Show jobs scheduled by `at` or `batch` commands."
content_hash: b0d439c3bd33f40ba6240516183cb2fe1e5510a5
related_topics:
  - title: italiano version
    url: /it/common/atq.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atq.html
    icon: bi bi-globe
---
# atq

Show jobs scheduled by `at` or `batch` commands.
More information: <https://man.archlinux.org/man/at.1>.

- Show the current user's scheduled jobs:

`atq`

- Show jobs from queue named 'a' (queues have single-character names):

`atq -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a</span>

- Show jobs of all users (run as superuser):

`sudo atq`
