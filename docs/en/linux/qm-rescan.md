---
layout: page
title: linux/qm-rescan (English)
description: "Rescan all storages and update disk sizes and unused disk images of a virtual machine."
content_hash: c20f5ace317798b6a80f4b6c4a0b46f9a54d82da
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm rescan

Rescan all storages and update disk sizes and unused disk images of a virtual machine.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Rescan all storages and update disk sizes and unused disk images of a specific virtual machine:

`qm rescan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Perform a dry-run of rescan on a specific virtual machine and do not write any changes to configurations:

`qm rescan --dryrun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
