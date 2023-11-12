---
layout: page
title: linux/rfkill (English)
description: "Enable and disable wireless devices."
content_hash: 255106a9e21f3365e18d57b3cb2161e737096ab5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rfkill

Enable and disable wireless devices.
More information: <https://manned.org/rfkill>.

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
