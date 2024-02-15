---
layout: page
title: linux/qm-guest-passwd (English)
description: "Set the password for a user on QEMU/KVM Virtual Machine Manager."
content_hash: 117fe75a86adefd1884afeda71c1e8e222927a0e
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# qm guest passwd

Set the password for a user on QEMU/KVM Virtual Machine Manager.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Set a password for a specific user in a virtual machine interactively:

`qm guest passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Set an already hashed password for a specific user in a virtual machine interactively:

`qm guest passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --crypted 1`
