---
layout: page
title: linux/synoupgrade (English)
description: "Upgrade Synology DiskStation Manager (DSM) - the Synology NAS operating system."
content_hash: 34a7e2de2a0c85fc617d319d51f95d42924624d6
last_modified_at: 2023-07-16
---
# synoupgrade

Upgrade Synology DiskStation Manager (DSM) - the Synology NAS operating system.
More information: <https://www.synology.com/dsm>.

- Check if upgrades are available:

`sudo synoupgrade --check`

- Check for patches without upgrading the DSM version:

`sudo synoupgrade --check-smallupdate`

- Download the latest upgrade available (use `--download-smallupdate` for patches):

`sudo synoupgrade --download`

- Start the upgrade process:

`sudo synoupgrade --start`

- Upgrade to the latest version automatically:

`sudo synoupgrade --auto`

- Apply patches without upgrading the DSM version automatically:

`sudo synoupgrade --auto-smallupdate`

- Upgrade the DSM using a patch file (should be an absolute path):

`sudo synoupgrade --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file.pat</span>

- Display help:

`synoupgrade`
