---
layout: page
title: common/vmtouch (English)
description: "Manage the filesystem cache."
content_hash: b677bc1594f07708a7d846268d47e3d6cf7fb849
last_modified_at: 2024-12-30
tldri18n_status: 2
---
# vmtouch

Manage the filesystem cache.
More information: <https://manned.org/vmtouch>.

- Print the cache status of a file:

`vmtouch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Load a file into cache:

`vmtouch -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Evict a file from cache:

`vmtouch -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Lock a file in cache to prevent eviction from memory:

`vmtouch -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Lock a file and daemonize the program:

`vmtouch -ld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
