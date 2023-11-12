---
layout: page
title: linux/qm-reboot (English)
description: "Reboot a virtual machine by shutting it down, and starting it again after applying pending changes."
content_hash: af11b3c22cdaf5d998d77d4c05c2246c458372f6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm reboot

Reboot a virtual machine by shutting it down, and starting it again after applying pending changes.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Reboot a virtual machine:

`qm reboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Reboot a virtual machine after wait for at most 10 seconds:

`qm reboot --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
