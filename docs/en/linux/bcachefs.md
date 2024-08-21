---
layout: page
title: linux/bcachefs (English)
description: "Manage `bcachefs` filesystems/devices."
content_hash: 555746bdcf4e743066d6ef14c034f0b9b149f06b
last_modified_at: 2024-08-21
tldri18n_status: 2
---
# bcachefs

Manage `bcachefs` filesystems/devices.
More information: <https://bcachefs.org/bcachefs-principles-of-operation.pdf>.

- Format a partition with `bcachefs`:

`sudo bcachefs format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Mount a `bcachefs` filesystem:

`sudo bcachefs mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mountpoint</span>

- Create a RAID 0 filesystem where an SSD acts as a cache and an HDD acts as a long-term storage:

`sudo bcachefs format --label=ssd.ssd1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ssd/partition</span>` --label=hdd.hdd1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hdd/partition</span>` --replicas=1 --foreground_target=ssd --promote_target=ssd --background_target=hdd`

- Mount a multidevice filesystem:

`sudo bcachefs mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mountpoint</span>

- Display disk usage:

`bcachefs fs usage --human-readable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mountpoint</span>

- Set replicas after formatting and mounting:

`sudo bcachefs set-fs-option --metadata_replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --data_replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Force `bcachefs` to ensure all files are replicated:

`sudo bcachefs data rereplicate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mountpoint</span>

- Display help:

`bcachefs`
