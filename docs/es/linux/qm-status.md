---
layout: page
title: linux/qm-status (español)
description: "Muestra el estado de una máquina virtual."
content_hash: aa304dcaa33a932ad1d6144ed50729a4344837b6
last_modified_at: 2024-12-14
related_topics:
  - title: English version
    url: /en/linux/qm-status.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-status.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-status.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm status

Muestra el estado de una máquina virtual.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Muestra el estado de una máquina virtual dada:

`qm status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Muestra el estado detallado de una máquina virtual dada:

`qm status --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>
