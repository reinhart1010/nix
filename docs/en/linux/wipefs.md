---
layout: page
title: linux/wipefs (English)
description: "Wipe filesystem, raid, or partition-table signatures from a device."
content_hash: e28a4fd67c09fd7d4da4ac4d612751d6338aa192
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wipefs

Wipe filesystem, raid, or partition-table signatures from a device.
More information: <https://manned.org/wipefs>.

- Display signatures for specified device:

`sudo wipefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Wipe all available signature types for a specific device with no recursion into partitions:

`sudo wipefs --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Wipe all available signature types for the device and partitions using a glob pattern:

`sudo wipefs --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>`*`

- Perform dry run:

`sudo wipefs --all --no-act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Force wipe, even if the filesystem is mounted:

`sudo wipefs --all --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
