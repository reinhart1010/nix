---
layout: page
title: linux/qm-guest-cmd (español)
description: "Ejecuta órdenes de agente huésped en QEMU."
content_hash: b24b643854b9d9eae9293c3b71d0234b2c9c774e
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/qm-guest-cmd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-guest-cmd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-guest-cmd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm guest cmd

Ejecuta órdenes de agente huésped en QEMU.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Ejecuta un comando específico de agente huésped en QEMU:

`qm guest cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_la_máquina_virtual</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fsfreeze-freeze|fsfreeze-status|fsfreeze-thaw|fstrim|get-fsinfo|...</span>
