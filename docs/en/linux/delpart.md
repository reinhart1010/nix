---
layout: page
title: linux/delpart (English)
description: "Ask the Linux kernel to forget about a partition."
content_hash: 363d9b5f6f393c1347503d2db778e3ff807d4552
last_modified_at: 2023-10-22
---
# delpart

Ask the Linux kernel to forget about a partition.
More information: <https://manned.org/delpart>.

- Tell the kernel to forget about the first partition of `/dev/sda`:

`sudo delpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
