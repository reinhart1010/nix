---
layout: page
title: linux/qm-reset (English)
description: "Reset a virtual machine on QEMU/KVM Virtual Machine Manager."
content_hash: 1b388c5a245ecbaf849715ee1b740169f64b6b34
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qm reset

Reset a virtual machine on QEMU/KVM Virtual Machine Manager.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Reset a virtual machine:

`qm reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Reset a virtual machine and skip lock (only root can use this option):

`qm reset --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
