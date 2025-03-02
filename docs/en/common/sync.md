---
layout: page
title: common/sync (English)
description: "Flushes all pending write operations to the appropriate disks."
content_hash: 7ad7bdb34d2c9c3fec13f03f967441af75de28e5
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/sync.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sync

Flushes all pending write operations to the appropriate disks.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/sync-invocation.html>.

- Flush all pending write operations on all disks:

`sync`

- Flush all pending write operations on a single file to disk:

`sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
