---
layout: page
title: linux/qm-shutdown (español)
description: "Apaga una máquina virtual del administrador de máquinas virtuales QEMU/KVM."
content_hash: 1b29933c53a76e952e07895cef96a884e65786cb
last_modified_at: 2024-12-15
related_topics:
  - title: English version
    url: /en/linux/qm-shutdown.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm shutdown

Apaga una máquina virtual del administrador de máquinas virtuales QEMU/KVM.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Apaga una máquina virtual:

`qm shutdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Apaga una máquina virtual después de esperar por lo menos 10 segundos:

`qm shutdown --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Apaga una máquina virtual y no desactiva los volúmenes de almacenamiento:

`qm shutdown --keepActive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Apaga una máquina virtual y omite cualquier bloqueo (solo el root puede usar esta opción):

`qm shutdown --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Detiene y apaga una máquina virtual:

`qm shutdown --forceStop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>
