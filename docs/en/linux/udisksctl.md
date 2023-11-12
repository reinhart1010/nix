---
layout: page
title: linux/udisksctl (English)
description: "Interact with `udisksd` to query and manipulate storage devices."
content_hash: b742ed9389acb4406e370fa1f896ce266a243ca4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# udisksctl

Interact with `udisksd` to query and manipulate storage devices.
More information: <http://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>.

- Show high-level information about disk drives and block devices:

`udisksctl status`

- Show detailed information about a device:

`udisksctl info --block-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Show detailed information about a device partition:

`udisksctl info --block-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Mount a device partition and prints the mount point:

`udisksctl mount --block-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Unmount a device partition:

`udisksctl unmount --block-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Monitor the daemon for events:

`udisksctl monitor`
