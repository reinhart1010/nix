---
layout: page
title: linux/qmrestore (English)
description: "Restore QemuServer vzdump backups."
content_hash: cb84635b10dc824e4be09ec43d2b29dcb681ad6d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/qmrestore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qmrestore

Restore QemuServer vzdump backups.
More information: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Restore virtual machine from given backup file on the original storage:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Overwrite existing virtual machine from a given backup file on the original storage:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --force true`

- Restore the virtual machine from a given backup file on specific storage:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local</span>

- Start virtual machine immediately from the backup while restoring in the background (only on Proxmox Backup Server):

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --live-restore true`
