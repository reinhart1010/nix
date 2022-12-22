---
layout: page
title: linux/qm-showcmd (English)
description: "Show command line which is used to start the VM (debug info)."
content_hash: e7bf9d0e36af9b4012386f725a2eb072df7e6c86
last_modified_at: 2022-12-22
---
# qm showcmd

Show command line which is used to start the VM (debug info).
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Show command line for a specific virtual machine:

`qm showcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Put each option on a new line to enhance human readability:

`qm showcmd --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Fetch config values from a specific snapshot:

`qm showcmd --snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
