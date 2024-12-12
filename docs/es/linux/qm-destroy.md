---
layout: page
title: linux/qm-destroy (español)
description: "Destruye una máquina virtual del administrador de máquinas virtuales EMU/KVM."
content_hash: 5d5abe0b513bb4ab81b292192930ae9009acff44
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/qm-destroy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-destroy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm destroy

Destruye una máquina virtual del administrador de máquinas virtuales EMU/KVM.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Destruye una máquina virtual específica:

`qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Destruye todos los discos que no se mencionan explícitamente en la configuración de una máquina virtual específica:

`qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` --destroy-unreferenced-disks`

- Destruye una máquina virtual y la elimina de todos los lugares (inventarios, trabajos de copia de seguridad, manejadores de alta disponibilidad, etc.):

`qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` --purge`

- Destruye una máquina virtual específica ignorando las cerraduras (locks) y forzando su destrucción:

`sudo qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` --skiplock`
