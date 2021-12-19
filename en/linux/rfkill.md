---
layout: page
title: linux/rfkill (English)
description: "Enable and disable wireless devices."
content_hash: daff7623a6c97e63cf2367bea5100d2115226d0c
---
# rfkill

Enable and disable wireless devices.

- List devices:

`rfkill`

- Filter by columns:

`rfkill -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID,TYPE,DEVICE</span>

- Block devices by type (e.g. bluetooth, wlan):

`rfkill block `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bluetooth</span>

- Unblock devices by type (e.g. bluetooth, wlan):

`rfkill unblock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan</span>

- Output in JSON format:

`rfkill -J`
