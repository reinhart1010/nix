---
layout: page
title: linux/qm-shutdown (English)
description: "Shutdown a virtual machine on QEMU/KVM Virtual Machine Manager."
content_hash: 05390b5aecad2bfdc876d997f45b065a2a6f1fb2
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qm shutdown

Shutdown a virtual machine on QEMU/KVM Virtual Machine Manager.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Shutdown a virtual machine:

`qm shutdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Shutdown a virtual machine after wait for at most 10 seconds:

`qm shutdown --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Shutdown a virtual machine and do not deactivate storage volumes:

`qm shutdown --keepActive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Shutdown a virtual machine and skip lock (only root can use this option):

`qm shutdown --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Stop and shutdown a virtual machine:

`qm shutdown --forceStop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>
