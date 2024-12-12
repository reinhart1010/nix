---
layout: page
title: linux/qm-migrate (español)
description: "Migra una máquina virtual."
content_hash: 9b108bc14bd1df00af4a73a4bfc0f793ef04e967
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/qm-migrate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-migrate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-migrate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm migrate

Migra una máquina virtual.
Se usa para crear una nueva tarea de migración.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Migra una máquina virtual específica:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>

- Supera el límite de ancho de banda E/S actual con 10 KiB/s:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` --bwlimit 10`

- Permite la migración de máquinas virtuales usando dispositivos locales (solo root):

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` --force true`

- Utiliza la migración en vivo (online) si una máquina virtual está ejecutándose:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` --online true`

- Permite la migración de almacenamiento en vivo para discos locales:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` --with-local-disks true`
