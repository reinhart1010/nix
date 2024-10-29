---
layout: page
title: common/ntpctl (English)
description: "Display information about the running instance of OpenNTPD."
content_hash: 0dcf097adab269601d7a11e96bd856a945acbc14
last_modified_at: 2024-10-29
tldri18n_status: 2
---
# ntpctl

Display information about the running instance of OpenNTPD.
More information: <https://man.openbsd.org/ntpctl>.

- Show all data:

`ntpctl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|all</span>

- Show information about each peer:

`ntpctl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">p|peers</span>

- Show the status of peers and sensors, and whether the system clock is synced:

`ntpctl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|status</span>

- Show information about each sensor:

`ntpctl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S|Sensors</span>
