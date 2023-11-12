---
layout: page
title: linux/qm-reset (English)
description: "Reset a virtual machine on QEMU/KVM Virtual Machine Manager."
content_hash: 1b388c5a245ecbaf849715ee1b740169f64b6b34
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm reset

Reset a virtual machine on QEMU/KVM Virtual Machine Manager.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Reset a virtual machine:

`qm reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Reset a virtual machine and skip lock (only root can use this option):

`qm reset --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
