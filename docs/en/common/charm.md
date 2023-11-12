---
layout: page
title: common/charm (English)
description: "Set of tools that makes adding a backend to your terminal-based applications, without worrying about user accounts, data storage and encryption."
content_hash: 279c853035921f75c355f732351c21ec0bc682e0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# charm

Set of tools that makes adding a backend to your terminal-based applications, without worrying about user accounts, data storage and encryption.
More information: <https://github.com/charmbracelet/charm>.

- Backup your Charm account keys:

`charm backup-keys`

- Backup Charm account keys to a specific location:

`charm backup-keys -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.tar</span>

- Import previously backed up Charm account keys:

`charm import-keys "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">charm-keys-backup.tar</span>`"`

- Find where your `cloud.charm.sh` folder resides on your machine:

`charm where`

- Start your Charm server:

`charm serve`

- Print linked SSH keys:

`charm keys`

- Print your Charm ID:

`charm id`
