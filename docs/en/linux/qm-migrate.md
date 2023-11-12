---
layout: page
title: linux/qm-migrate (English)
description: "Migrate a virtual machine."
content_hash: e1e7cd8fe71591cb5e0cb33abc2daa045dfcb225
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm migrate

Migrate a virtual machine.
Used to create a new migration task.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Migrate a specific virtual machine:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Override the current I/O bandwidth limit with 10 KiB/s:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --bwlimit 10`

- Allow migration of virtual machines using local devices (root only):

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --force true`

- Use online/live migration if a virtual machine is running:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --online true`

- Enable live storage migration for local disks:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --with-local-disks true`
