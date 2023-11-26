---
layout: page
title: linux/qm-disk-move (Nederlands)
description: "Verplaats een virtuele schijf van de ene opslag naar de andere binnen hetzelfde Proxmox cluster."
content_hash: 044811fbf82325a2163f8cc61c0bfdb9a9880458
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/linux/qm-disk-move.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm disk move

Verplaats een virtuele schijf van de ene opslag naar de andere binnen hetzelfde Proxmox cluster.
Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Verplaats een virtuele schijf:

`qm disk move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestemming</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index</span>

- Verwijder de vorige kopie van de virtuele schijf:

`qm disk move -delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestemming</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index</span>
