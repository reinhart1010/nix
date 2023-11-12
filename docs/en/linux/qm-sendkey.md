---
layout: page
title: linux/qm-sendkey (English)
description: "Send QEMU monitor encoding key event to a virtual machine."
content_hash: 78083361b8e3c7fd96fb138fd783039b43df3b04
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm sendkey

Send QEMU monitor encoding key event to a virtual machine.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Send the specified key event to a specific virtual machine:

`qm sendkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Allow root user to send key event and ignore locks:

`qm sendkey --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>
