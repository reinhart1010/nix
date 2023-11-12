---
layout: page
title: linux/qm-destroy (English)
description: "Destroy a virtual machine in QEMU/KVM Virtual Machine Manager."
content_hash: 1f49e1f44b3d02c0c99d69cdb2654549b9a0765d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm destroy

Destroy a virtual machine in QEMU/KVM Virtual Machine Manager.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Destroy a specific virtual machine:

`qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Destroy all disks that are not explicitly referenced in a specific virtual machine's configuration:

`qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` --destroy-unreferenced-disks`

- Destroy a virtual machine and remove from all locations (inventory, backup jobs, high availability managers, etc.):

`qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` --purge`

- Destroy a specific virtual machine ignoring locks and forcing destroy:

`sudo qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` --skiplock`
