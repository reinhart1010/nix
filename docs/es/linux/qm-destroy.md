---
layout: page
title: linux/qm-destroy (español)
description: "Destruye una máquina virtual del administrador de máquinas virtuales EMU/KVM."
content_hash: 5d5abe0b513bb4ab81b292192930ae9009acff44
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/qm-destroy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-destroy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-destroy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm destroy

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
