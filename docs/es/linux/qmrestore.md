---
layout: page
title: linux/qmrestore (español)
description: "Restaura copias de seguridad de QemuServer `vzdump`."
content_hash: 8643a3b367a66830957abaa07814640a45d41515
last_modified_at: 2024-12-13
related_topics:
  - title: Deutsch version
    url: /de/linux/qmrestore.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/qmrestore.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qmrestore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qmrestore

Restaura copias de seguridad de QemuServer `vzdump`.
Más información: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Restaura la máquina virtual desde un archivo de respaldo dado en el almacenamiento original:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Sobrescribe la máquina virtual existente desde un archivo de respaldo dado en el almacenamiento original:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --force true`

- Restaura la máquina virtual de un archivo de respaldo dado en el almacenamiento específico:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local</span>

- Inicia la máquina virtual de inmediato desde la copia de seguridad mientras se restaura en el fondo (background) (sólo en el servidor de respaldo Proxmox):

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --live-restore true`
