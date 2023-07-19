---
layout: page
title: linux/qm-disk-import (English)
description: "Import a disk image to a virtual machine as an unused disk."
content_hash: 43f25b73fbe6d6d6fe44f38677b39f13af4c157f
last_modified_at: 2023-07-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qm disk import

Import a disk image to a virtual machine as an unused disk.
The supported image formats for `qemu-img`, such as raw, qcow2, qed, vdi, vmdk, and vhd must be used.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Import a VMDK/qcow2/raw disk image using a specific storage name:

`qm importdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/disk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_name</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qcow2|raw|vmdk</span>
