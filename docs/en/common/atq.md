---
layout: page
title: common/atq (English)
description: "Show jobs scheduled by `at` or `batch` commands."
content_hash: c85099d671f97220771c39d5374368a21023f9cc
last_modified_at: 2024-02-09
related_topics:
  - title: فارسی version
    url: /fa/common/atq.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atq.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atq.html
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

- Show jobs from the 'a' [q]ueue (queues have single-character names):

`atq -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a</span>

- Show jobs of all users (run as superuser):

`sudo atq`
