---
layout: page
title: linux/blkdiscard (English)
description: "Discards device sectors on storage devices. Useful for SSDs."
content_hash: 95d07d8e674a1cd762afef9f81afbe3e9ad5b372
last_modified_at: 2023-11-12
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

`blkdiscard /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Securely discard all blocks on a device, removing all data:

`blkdiscard --secure /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Discard the first 100 MB of a device:

`blkdiscard --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100MB</span>` /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>
