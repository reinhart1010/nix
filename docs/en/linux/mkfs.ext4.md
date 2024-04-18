---
layout: page
title: linux/mkfs.ext4 (English)
description: "Create an ext4 filesystem inside a partition."
content_hash: 93a9fb5b03a501b52e1e4a985cd0f44ff1b8d98c
last_modified_at: 2024-04-18
related_topics:
  - title: Indonesia version
    url: /id/linux/mkfs.ext4.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.ext4.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.ext4

Create an ext4 filesystem inside a partition.
More information: <https://manned.org/mkfs.ext4>.

- Create an ext4 filesystem inside partition 1 on device b (`sdb1`):

`sudo mkfs.ext4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create an ext4 filesystem with a volume-label:

`sudo mkfs.ext4 -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
