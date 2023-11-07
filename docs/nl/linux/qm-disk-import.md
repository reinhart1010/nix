---
layout: page
title: linux/qm-disk-import (Nederlands)
description: "Importeer een schijf image in een virtuele machine als een ongebruikte schijf."
content_hash: adcfe38981a768a92fe61fbb084d886e4f062140
last_modified_at: 2023-11-07
related_topics:
  - title: English version
    url: /en/linux/qm-disk-import.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qm disk import

Importeer een schijf image in een virtuele machine als een ongebruikte schijf.
De onderstende image formaten voor `qemu-img`, zoals raw, qcow2, qed, vdi, vmdk, en vhd moeten gebruikt worden.
Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Importeer een VMDK/qcow2/raw schijf image met behulp van een specifieke opslagnaam:

`qm importdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/schijf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opslagnaam</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qcow2|raw|vmdk</span>
