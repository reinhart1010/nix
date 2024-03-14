---
layout: page
title: linux/qm-suspend (English)
description: "Suspends a virtual machine (VM) in the Proxmox Virtual Environment (PVE)."
content_hash: 8835f29a631a9b3dd2b0937c40851f689179329f
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# qm suspend

Suspends a virtual machine (VM) in the Proxmox Virtual Environment (PVE).
Use `--skiplock` and `--skiplockstorage` flags with caution, as they may lead to data corruption in certain situations.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Suspend a virtual machine by ID:

`qm suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integer</span>

- Skip the lock check when suspending the VM:

`qm suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integer</span>` --skiplock`

- Skip the lock check for storage when suspending the VM:

`qm suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integer</span>` --skiplockstorage`
