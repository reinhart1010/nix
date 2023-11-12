---
layout: page
title: linux/btrfs-scrub (English)
description: "Scrub btrfs filesystems to verify data integrity."
content_hash: 5b47e5025b7e3557947b11f98c583be04310d3f8
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-scrub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs scrub

Scrub btrfs filesystems to verify data integrity.
It is recommended to run a scrub once a month.
More information: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Start a scrub:

`sudo btrfs scrub start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>

- Show the status of an ongoing or last completed scrub:

`sudo btrfs scrub status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>

- Cancel an ongoing scrub:

`sudo btrfs scrub cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>

- Resume a previously cancelled scrub:

`sudo btrfs scrub resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>

- Start a scrub, but wait until the scrub finishes before exiting:

`sudo btrfs scrub start -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>

- Start a scrub in quiet mode (does not print errors or statistics):

`sudo btrfs scrub start -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>
