---
layout: page
title: linux/qmrestore (English)
description: "Restore QemuServer `vzdump` backups."
content_hash: f12965bb382016b85a2380fff28d762b08fa0d7b
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/linux/qmrestore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qmrestore

Restore QemuServer `vzdump` backups.
More information: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Restore virtual machine from given backup file on the original storage:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Overwrite existing virtual machine from a given backup file on the original storage:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --force true`

- Restore the virtual machine from a given backup file on specific storage:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local</span>

- Start virtual machine immediately from the backup while restoring in the background (only on Proxmox Backup Server):

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --live-restore true`
