---
layout: page
title: linux/bwrap (English)
description: "Run programs in a lightweight sandbox."
content_hash: 87f95e75d858dbf327fc3fae79916c7c755cbdca
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/bwrap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bwrap

Run programs in a lightweight sandbox.
More information: <https://manned.org/bwrap>.

- Run a program in a read-only environment:

`bwrap --ro-bind / / `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Give the environment access to devices, process information and create a `tmpfs` for it:

`bwrap --dev-bind /dev /dev --proc /proc --ro-bind / / --tmpfs /tmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>
