---
layout: page
title: linux/cfdisk (English)
description: "Manage partition tables and partitions on a hard disk using a curses UI."
content_hash: 43041692258b98d9b793837977296084306b52cb
last_modified_at: 2024-02-25
related_topics:
  - title: Deutsch version
    url: /de/linux/cfdisk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/cfdisk.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cfdisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cfdisk

Manage partition tables and partitions on a hard disk using a curses UI.
More information: <https://manned.org/cfdisk>.

- Start the partition manipulator with a specific device:

`cfdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Create a new partition table for a specific device and manage it:

`cfdisk --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
