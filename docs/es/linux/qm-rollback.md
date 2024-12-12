---
layout: page
title: linux/qm-rollback (español)
description: "Revierte el estado de la máquina virtual (MV) a una instantánea (snapshot) específica."
content_hash: 8d80830cd7bae1348bbe7dc78e101ee4789f5080
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/qm-rollback.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-rollback.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-rollback.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm rollback

Revierte el estado de la máquina virtual (MV) a una instantánea (snapshot) específica.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Revierte el estado de una MV a una instantánea dada:

`qm rollback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_instantánea</span>
