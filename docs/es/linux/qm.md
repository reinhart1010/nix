---
layout: page
title: linux/qm (español)
description: "Administrador de máquinas virtuales QEMU/KVM."
content_hash: 8b18b0d06192f4441c07d31b5a94ed5de8054377
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/qm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm

Administrador de máquinas virtuales QEMU/KVM.
Algunas órdenes como `list`, `start`, `stop`, `clone`, etc. tienen su propia documentación.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Lista todas las máquinas virtuales:

`qm list`

- Dado un archivo ISO subido en el almacenamiento local, crea una máquina virtual con un disco IDE de 4 GB en el almacenamiento `local-lvm` y con ID 100:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` -ide0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local-lvm:4</span>` -net0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000</span>` -cdrom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local:iso/proxmox-mailgateway_2.1.iso</span>

- Muestra la configuración de una máquina virtual especificando su ID:

`qm config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Inicia una máquina virtual específica:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Envía una solicitud de apagado, luego espera hasta que se detenga la máquina virtual:

`qm shutdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` && qm wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Destruye una máquina virtual y elimina todos los recursos relacionados:

`qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --purge`
