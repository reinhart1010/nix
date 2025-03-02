---
layout: page
title: linux/kmod (English)
description: "Manage Linux kernel modules."
content_hash: 4257a4ca42d3fe909f310ee5e2a361cc2a743757
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/kmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kmod

Manage Linux kernel modules.
This program is usually called via its symlinks: `lsmod`, `rmmod`, `insmod`, `modinfo`, `modprobe`, and `depmod`.
See their respective pages for more information.
More information: <https://manned.org/kmod>.

- List currently loaded kernel modules:

`kmod list`

- Display the static device nodes information provided by the modules of the currently running kernel:

`kmod static-nodes`
