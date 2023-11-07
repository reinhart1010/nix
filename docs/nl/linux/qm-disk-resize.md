---
layout: page
title: linux/qm-disk-resize (Nederlands)
description: "Wijzig de grote van een virtuele machine schijf in the Proxmox Virtual Environment (PVE)."
content_hash: 4bc2e3e704e184a21445a6a5cbf8155ce96af3cd
last_modified_at: 2023-11-07
related_topics:
  - title: English version
    url: /en/linux/qm-disk-resize.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qm disk resize

Wijzig de grote van een virtuele machine schijf in the Proxmox Virtual Environment (PVE).
Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Voeg `n` gigabytes toe aan een virtuele schijf:

`qm disk resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schijfnaam</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`G`
