---
layout: page
title: linux/qmrestore (English)
description: "Restore QemuServer vzdump Backups."
content_hash: a5e0d96aa4fb32b46f30906f6bd24d6866c2e20e
---
# qmrestore

Restore QemuServer vzdump Backups.
More information: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Restore KVM-based virtual machine to local storage:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/lib/vz/dump/backup_file.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` --storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local</span>
