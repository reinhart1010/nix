---
layout: page
title: linux/qm (English)
description: "QEMU/KVM Virtual Machine Manager."
content_hash: a7b9c95a72457efc2b85ec46a62f3d1dbc56b24a
last_modified_at: 2024-10-05
tldri18n_status: 2
---
# qm

QEMU/KVM Virtual Machine Manager.
Some subcommands such as `list`, `start`, `stop`, `clone`, etc. have their own usage documentation.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- List all virtual machines:

`qm list`

- Using an ISO file uploaded on the local storage, create a virtual machine with a 4 GB IDE disk on the `local-lvm` storage and an ID of 100:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` -ide0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local-lvm:4</span>` -net0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000</span>` -cdrom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local:iso/proxmox-mailgateway_2.1.iso</span>

- Show the configuration of a virtual machine, specifying its ID:

`qm config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Start a specific virtual machine:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Send a shutdown request, then wait until the virtual machine is stopped:

`qm shutdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` && qm wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Destroy a virtual machine and remove all related resources:

`qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --purge`
