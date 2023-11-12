---
layout: page
title: linux/qm-snapshot (English)
description: "Create virtual machine snapshots."
content_hash: 86017e2dc8f311d894e41d5d8d91322173652441
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm snapshot

Create virtual machine snapshots.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Create a snapshot of a specific virtual machine:

`qm snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>

- Create a snapshot with a specific description:

`qm snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>` --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>

- Create a snapshot including the vmstate:

`qm snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>` --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>` --vmstate 1`
