---
layout: page
title: linux/boltctl (English)
description: "Control thunderbolt devices."
content_hash: 9b8ee058f8bd7fd20f181a08a31ae134ee3f98fc
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/boltctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# boltctl

Control thunderbolt devices.
More information: <https://manned.org/boltctl>.

- List connected (and authorized) devices:

`boltctl`

- List connected devices, including unauthorized ones:

`boltctl list`

- Authorize a device temporarily:

`boltctl authorize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_uuid</span>

- Authorize and remember a device:

`boltctl enroll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_uuid</span>

- Revoke a previously authorized device:

`boltctl forget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_uuid</span>

- Show more information about a device:

`boltctl info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_uuid</span>
