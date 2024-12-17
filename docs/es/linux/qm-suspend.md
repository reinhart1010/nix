---
layout: page
title: linux/qm-suspend (español)
description: "Suspende una máquina virtual (MV) en el entorno virtual Proxmox (PVE)."
content_hash: cd1fb1e7e133211e31a86140c02d09a1d480de19
last_modified_at: 2024-12-17
related_topics:
  - title: English version
    url: /en/linux/qm-suspend.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-suspend.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm suspend

Suspende una máquina virtual (MV) en el entorno virtual Proxmox (PVE).
Usa las banderas de `--skiplock` y `--skiplockstorage` con precaución, ya que pueden conducir a la corrupción de datos en ciertas situaciones.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Suspende una máquina virtual por ID:

`qm suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entero</span>

- Omite el chequeo de bloqueo al suspender una MV:

`qm suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entero</span>` --skiplock`

- Omite el chequeo de bloqueo por almacenamiento al suspender una MV:

`qm suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entero</span>` --skiplockstorage`
