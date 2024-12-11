---
layout: page
title: linux/qm-guest-passwd (español)
description: "Establece la contraseña para un usuario en el administrador de máquinas virtuales QEMU/KVM."
content_hash: 0194ee19abfcd251f0a0f9a82ecbaef9e84523a8
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/qm-guest-passwd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-guest-passwd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-guest-passwd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm guest passwd

Establece la contraseña para un usuario en el administrador de máquinas virtuales QEMU/KVM.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Establece una contraseña para un usuario específico en una máquina virtual de forma interactiva:

`qm guest passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Establece una contraseña ya procesada (hashed) para un usuario específico en una máquina virtual de forma interactiva:

`qm guest passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --crypted 1`
