---
layout: page
title: linux/qm-reset (español)
description: "Reinicia una máquina virtual en el administrador de máquinas virtuales QEMU/KVM."
content_hash: 89f4858d3b8581952c33f4a7377b02f195abd5c3
last_modified_at: 2024-12-13
related_topics:
  - title: English version
    url: /en/linux/qm-reset.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-reset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm reset

Reinicia una máquina virtual en el administrador de máquinas virtuales QEMU/KVM.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Restablece una máquina virtual:

`qm reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Reinicia una máquina virtual y omite cualquier bloqueo (solo el root puede usar esta opción):

`qm reset --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>
