---
layout: page
title: common/atq (English)
description: "Show jobs scheduled by `at` or `batch` commands."
content_hash: 48ad6cf8910e080cccf922eb3ebaf3c2db5a3e65
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/atq.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atq.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atq

Show jobs scheduled by `at` or `batch` commands.
More information: <https://manned.org/atq>.

- Show the current user's scheduled jobs:

`atq`

- Show jobs from queue named 'a' (queues have single-character names):

`atq -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a</span>

- Show jobs of all users (run as superuser):

`sudo atq`
