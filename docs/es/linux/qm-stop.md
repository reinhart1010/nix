---
layout: page
title: linux/qm-stop (español)
description: "Detiene una máquina virtual."
content_hash: 9ad6848fbd5bd91e0795d97b703120b4dc870ebd
last_modified_at: 2024-12-15
related_topics:
  - title: English version
    url: /en/linux/qm-stop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-stop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm stop

Detiene una máquina virtual.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Detiene una máquina virtual inmediatamente:

`qm stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Detiene una máquina virtual y espera por lo menos 10 segundos:

`qm stop --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Detiene una máquina virtual y omite cualquier bloqueo (solo el root puede usar esta opción):

`qm stop --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Detiene una máquina virtual y no desactive los volúmenes de almacenamiento:

`qm stop --keepActive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>
