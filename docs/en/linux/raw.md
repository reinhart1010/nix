---
layout: page
title: linux/raw (English)
description: "Bind a Unix raw character device."
content_hash: eea217eb92697fce4a82bbfe1ca1ce3c615f1afb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# raw

Bind a Unix raw character device.
More information: <https://manned.org/raw.8>.

- Bind a raw character device to a block device:

`raw /dev/raw/raw`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/block_device</span>

- Query an existing binding instead of setting a new one:

`raw /dev/raw/raw`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Query all bound raw devices:

`raw -qa`
