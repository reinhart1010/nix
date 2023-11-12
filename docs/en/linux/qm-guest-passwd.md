---
layout: page
title: linux/qm-guest-passwd (English)
description: "Set the password for a specific user on QEMU/KVM Virtual Machine Manager."
content_hash: 43e648ec58727c697366346688c7f6d62c4eea4c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm guest passwd

Set the password for a specific user on QEMU/KVM Virtual Machine Manager.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Set a password for a specific user in a virtual machine interactively:

`qm guest passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Set an already hashed password for a specific user in a virtual machine interactively:

`qm guest passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --crypted 1`
