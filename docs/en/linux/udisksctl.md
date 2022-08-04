---
layout: page
title: linux/udisksctl (English)
description: "A command-line program used to interact with the udisksd daemon process."
content_hash: f6d64b36188eae094715bf88047c11ecc5d754da
---
# udisksctl

A command-line program used to interact with the udisksd daemon process.
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
