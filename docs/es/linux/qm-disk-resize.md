---
layout: page
title: linux/qm-disk-resize (español)
description: "Redimensiona un disco de máquina virtual en el entorno virtual Proxmox (PVE)."
content_hash: 6b474f659835662659b70a410d38c1fd5912640c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/qm-disk-resize.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-disk-resize.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/qm-disk-resize.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-disk-resize.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm disk resize

Redimensiona un disco de máquina virtual en el entorno virtual Proxmox (PVE).
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Añade `n` gigabytes a un disco virtual:

`qm disk resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_disco</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`G`
