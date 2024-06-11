---
layout: page
title: linux/blkdiscard (English)
description: "Discards device sectors on storage devices. Useful for SSDs."
content_hash: 8c7d5c848ff4bc4c282900c888eabfc8e586f438
last_modified_at: 2024-06-11
related_topics:
  - title: 中文 version
    url: /zh/linux/blkdiscard.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blkdiscard

Discards device sectors on storage devices. Useful for SSDs.
More information: <https://manned.org/blkdiscard>.

- Discard all sectors on a device, removing all data:

`blkdiscard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device</span>

- Securely discard all blocks on a device, removing all data:

`blkdiscard --secure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device</span>

- Discard the first 100 MB of a device:

`blkdiscard --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100MB</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device</span>
