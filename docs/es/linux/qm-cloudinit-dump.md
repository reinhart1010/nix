---
layout: page
title: linux/qm-cloudinit-dump (español)
description: "Genera archivos de configuración Cloudinit."
content_hash: cc655bb16b3b06f20a3ecfdbe73947240524e68f
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/qm-cloudinit-dump.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-cloudinit-dump.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-cloudinit-dump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm cloudinit dump

Genera archivos de configuración Cloudinit.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Genera un archivo cloudinit para un tipo de configuración específica:

`qm cloudinit dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_máquina_virtual</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meta|network|user</span>
