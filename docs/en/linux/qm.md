---
layout: page
title: linux/qm (English)
description: "Qemu/KVM Virtual Machine Manager."
content_hash: 12f30b0739716808891860ba47c3de1b90f3cb36
---
# qm

Qemu/KVM Virtual Machine Manager.
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
