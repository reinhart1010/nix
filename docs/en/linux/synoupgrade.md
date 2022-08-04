---
layout: page
title: linux/synoupgrade (English)
description: "Upgrade a Synology DiskStation Manager (DSM) from the command-line."
content_hash: 0f613a42c8fd2c27da7f4738f5330adc5d96e8a2
---
# synoupgrade

Upgrade a Synology DiskStation Manager (DSM) from the command-line.
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
