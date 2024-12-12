---
layout: page
title: linux/qm-cleanup (español)
description: "Limpia recursos en el Administrador de máquinas virtuales QEMU/KVM como dispositivos tap, VGPUs, etc."
content_hash: 32c48ff38cf1541c6e1bd9b6adcca5af6c820676
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/qm-cleanup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-cleanup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm cleanup

Limpia recursos en el Administrador de máquinas virtuales QEMU/KVM como dispositivos tap, VGPUs, etc.
Usualmente se lo utiliza después de que una VM se apaga, se rompe, etc.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Limpia los recursos:

`qm cleanup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clean-shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest-requested</span>
