---
layout: page
title: linux/qm-create (español)
description: "Crea o restaura una máquina virtual en el administrador de máquinas virtuales QEMU/KVM."
content_hash: 2ed954eb2d600a09ac764c4995ee6ce19b12d00f
last_modified_at: 2024-12-12
related_topics:
  - title: Deutsch version
    url: /de/linux/qm-create.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/qm-create.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm create

Crea o restaura una máquina virtual en el administrador de máquinas virtuales QEMU/KVM.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Crea una máquina virtual:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Inicia automáticamente la máquina después de su creación:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --start 1`

- Especifica el tipo de sistema operativo en la máquina virtual:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --ostype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">win10</span>

- Reemplaza una máquina existente (requiere archivarla):

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_respaldo.tar</span>` --force 1`

- Especifica un guión (script) a ejecutar automáticamente dependiendo del estado de la máquina virtual:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --hookscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/guión.pl</span>
