---
layout: page
title: linux/qm-guest-exec-status (español)
description: "Imprime el estado de un pid iniciado por el agente huésped en el administrador de máquinas virtuales QEMU/KVM."
content_hash: 8ad7815095e49a4e6e5079477a1741aed6a73bc4
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/qm-guest-exec-status.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-guest-exec-status.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-guest-exec-status.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm guest exec-status

Imprime el estado de un pid iniciado por el agente huésped en el administrador de máquinas virtuales QEMU/KVM.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Imprime el estado de un PID específico:

`qm guest exec-status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
