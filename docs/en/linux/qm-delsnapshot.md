---
layout: page
title: linux/qm-delsnapshot (English)
description: "Delete virtual machine snapshots."
content_hash: 3e7aff8257ed4531d0536dd477bd0b37bdffb52e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm delsnapshot

Delete virtual machine snapshots.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Delete a snapshot:

`qm delsnapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>

- Delete a snapshot from a configuration file (even if removing the disk snapshot fails):

`qm delsnapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>` --force 1`
