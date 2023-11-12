---
layout: page
title: linux/qm-resume (English)
description: "Resume a virtual machine."
content_hash: f9fbd7ea4135d9f00a004a1c990be9c4ff4f5e3f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm resume

Resume a virtual machine.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Resume a specific virtual machine:

`qm resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Resume a specific virtual machine ignoring locks (requires root):

`sudo qm resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` --skiplock true`
