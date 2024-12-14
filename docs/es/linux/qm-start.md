---
layout: page
title: linux/qm-start (español)
description: "Inicia una máquina virtual en el administrador de máquinas virtuales QEMU/KVM."
content_hash: b7b1eb381306a68c3fc8d1755c1e3ec8a07d136c
last_modified_at: 2024-12-14
related_topics:
  - title: Deutsch version
    url: /de/linux/qm-start.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/qm-start.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-start.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-start.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm start

Inicia una máquina virtual en el administrador de máquinas virtuales QEMU/KVM.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Inicia una máquina virtual específica:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Especifica el tipo de máquina QEMU (es decir, la CPU a emular):

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">q35</span>

- Comienza una máquina virtual específica con un tiempo de espera máximo de 60 segundos:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>
