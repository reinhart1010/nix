---
layout: page
title: linux/systemd-repart (English)
description: "Automatically grow and add partitions."
content_hash: 4fe0f329ab85890eda364c1d9020e3e5d8452799
last_modified_at: 2023-10-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemd-repart

Automatically grow and add partitions.
Grows and adds partitions based on the configuration files described in repart.d.
Does not automatically resize file system on partition. See systemd-growfs to extend file system.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-repart.html>.

- Grow the root partition (/) to all available disk space:

`systemd-repart`

- View changes without applying:

`systemd-repart --dry-run=yes`

- Grow root partition size to 10 gigabytes:

`systemd-repart --size=10G --root /`
