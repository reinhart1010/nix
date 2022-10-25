---
layout: page
title: linux/qm-rollback (English)
description: "Rollback the VM state to a specified snapshot."
content_hash: e0b287a7282748878eeb21da28108f2393df5912
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qm rollback

Rollback the VM state to a specified snapshot.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Rollback the state of a specific VM to a specified snapshot:

`qm rollback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snap_name</span>
