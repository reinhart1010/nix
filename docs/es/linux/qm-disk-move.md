---
layout: page
title: linux/qm-disk-move (español)
description: "Mueve un disco virtual de un almacenamiento a otro dentro del mismo grupo Proxmox."
content_hash: 64163215300da0756f12b372d8a791e06a27922f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/qm-disk-move.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-disk-move.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/qm-disk-move.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm disk move

Mueve un disco virtual de un almacenamiento a otro dentro del mismo grupo Proxmox.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Mueve un disco virtual:

`qm disk move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">índice</span>

- Elimina la copia anterior del disco virtual:

`qm disk move -delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">índice</span>
