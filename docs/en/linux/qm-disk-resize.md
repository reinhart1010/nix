---
layout: page
title: linux/qm-disk-resize (English)
description: "Resize a virtual machine disk in the Proxmox Virtual Environment (PVE)."
content_hash: 8e727e5bafee7c2248e11ac9f3786db0963689f2
last_modified_at: 2023-07-14
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qm disk resize

Resize a virtual machine disk in the Proxmox Virtual Environment (PVE).
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Add `n` gigabytes to a virtual disk:

`qm disk resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disk_name</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`G`
