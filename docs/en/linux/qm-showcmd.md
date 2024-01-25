---
layout: page
title: linux/qm-showcmd (English)
description: "Show command-line which is used to start the VM (debug info)."
content_hash: 5682b6d035ee83c7aadf88a63d93753d1db3358f
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# qm showcmd

Show command-line which is used to start the VM (debug info).
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Show command-line for a specific virtual machine:

`qm showcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Put each option on a new line to enhance human readability:

`qm showcmd --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Fetch configuration values from a specific snapshot:

`qm showcmd --snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
