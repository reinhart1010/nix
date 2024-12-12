---
layout: page
title: linux/qm-reboot (español)
description: "Reinicia una máquina virtual cerrándola, y arrancando de nuevo después de aplicar cambios pendientes."
content_hash: 4ba34a242dab8c4bea4aa5c6c15a42d382bdc7e1
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/qm-reboot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-reboot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-reboot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm reboot

Reinicia una máquina virtual cerrándola, y arrancando de nuevo después de aplicar cambios pendientes.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Reinicia una máquina virtual:

`qm reboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Reinicia una máquina virtual después de esperar por lo menos 10 segundos:

`qm reboot --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>
