---
layout: page
title: linux/wipefs (English)
description: "Wipe filesystem, raid, or partition-table signatures from a device."
content_hash: 1a4b317a979149fd6207e84c030fbaea0b6361b8
---
# wipefs

Wipe filesystem, raid, or partition-table signatures from a device.
More information: <https://manned.org/wipefs>.

- Display signatures for specified device:

`sudo wipefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Wipe all available signatures for specified device:

`sudo wipefs --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Perform dry run:

`sudo wipefs --all --no-act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Force wipe, even if the filesystem is mounted:

`sudo wipefs --all --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
